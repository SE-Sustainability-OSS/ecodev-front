""" 
Elements to display Sankey diagrams
"""

import networkx as nx
import pandas as pd
import plotly.graph_objects as go
from ecodev_core import Frozen
from networkx.classes.digraph import DiGraph
from pydantic import BaseModel

from ecodev_core import logger_get
log = logger_get(__name__)

class GraphInfo(BaseModel):
    """
    A simple graph (either node or edge) information: a color, a label and a value
    """
    color: str
    label: str
    value: float


class GraphConf(Frozen):
    """
    configuration to generate a Directed Acyclic Graph out of a flatten df version of it.
    Attributes are:
        - sankey_columns: the columns used to generate the dag. A hierarchy is expected between the
          columns, like in Entity 1, Entity 2, Entity 3... Where Entity 2 is a refinement
          of Entity 1 and Entity 3 of Entity 2.
        - filter_columns: if empty, the full flatten df data will be used. If not, filtering
          operations will exclude data not specified here. Given a key and it's associated list
          of values, only df[df[key].isin(values)] are kept.
        - quant_column: quantitative column to be used that gives values to graph nodes and edges.
        - colors: a list of colors in which to pick to color the graph nodes and edges
          in it's sankey representation
        - thresh: All edges and nots with values smaller than this threshold are discarded.
    """
    sankey_columns: list[str]
    filter_columns: dict[str, list[str]] = {}
    quant_column: str
    colors: list[str]
    thresh: float = 0.1


def create_graph_from_columns(raw_df: pd.DataFrame, conf: GraphConf) -> DiGraph:
    """
    Create a graph out of the passed dataframe, given a GraphConf.
    NB: We create a root node to ease the DAG generation
    """
    df = raw_df.copy()
    for col, values in conf.filter_columns.items():
        df = df[df[col].isin(values)]

    graph = nx.DiGraph()
    graph.add_nodes_from([(0, GraphInfo(color=conf.colors[0], value=100, label='root'))])

    for depth, column in enumerate(conf.sankey_columns):
        add_nodes_from_column(graph, df, column, depth, conf)

    add_edges_from_columns(graph, df, conf)
    add_colors(graph)
    return graph


def add_nodes_from_column(graph: DiGraph,
                          df: pd.DataFrame,
                          column: str,
                          depth: int,
                          conf: GraphConf
                          ) -> None:
    """
    Add nodes to the passed graph corresponding to column in df.
    NB: subtlety for the higher level depth: in that case we want to create edges between those
       high level nodes and the dag root node.
    NB2: here we do not sort in ascending order the nodes wrt to the quantitative column,
     as we color them in this order (and we would rather prefer to have the nodes with the
     highest value wrt to the quantitative column to color their children than the other way around
    """
    tmp = df[[column, conf.quant_column]].groupby(column)[conf.quant_column].sum().reset_index()
    for jdx, row in tmp[tmp[conf.quant_column] > conf.thresh].sort_values(
            conf.quant_column).iterrows():
        graph.add_nodes_from([(len(graph.nodes),
                               GraphInfo(color=conf.colors[jdx % len(conf.colors)],
                                         value=row[conf.quant_column],
                                         label=row[column]))])
        if depth == 0:
            graph.add_edges_from([(0, len(graph.nodes) - 1, GraphInfo(
                color=conf.colors[0], value=row[conf.quant_column],
                label=f'source: root, target: {row[column]}'))])


def add_edges_from_columns(graph: DiGraph, df: pd.DataFrame, conf: GraphConf) -> None:
    """
    Add all edges (not related to root) to the passed graph.
    """
    nodes = {graph.nodes[node]['label']: node for node in graph.nodes}
    for first_col, second_col in zip(conf.sankey_columns, conf.sankey_columns[1:]):
        add_edges_from_column_pairs(graph, df, first_col, second_col, nodes, conf)


def add_edges_from_column_pairs(graph: DiGraph,
                                df: pd.DataFrame,
                                f_col: str,
                                s_col: str,
                                nodes: dict[str, int],
                                conf: GraphConf
                                ) -> None:
    """
    Add all edges between nodes of f_col and s_col in the flatten df data.
    NB: Beware, huge subtlety, we forbid here cycles. To be discussed further
    """
    tmp = df[[f_col, s_col, conf.quant_column]].groupby(
        [f_col, s_col])[conf.quant_column].sum().reset_index()
    for _, row in tmp[tmp[conf.quant_column] > conf.thresh].sort_values(
            conf.quant_column, ascending=False).iterrows():
        if row[f_col] != row[s_col]:
            graph.add_edges_from([(nodes[row[f_col]], nodes[row[s_col]],
                                   GraphInfo(color=conf.colors[0], value=row[conf.quant_column],
                                             label=f'source: {row[f_col]}, target: {row[s_col]}'))])


def add_colors(graph: DiGraph) -> None:
    """
    Add all edges colors for all edges not related to root.
    """
    for node in [x for x in nx.dfs_preorder_nodes(graph, source=0, depth_limit=1) if x != 0]:
        for edge in [x for x in nx.dfs_edges(graph, source=node)]:
            graph.edges[edge]['color'] = graph.nodes[node]['color']


def get_sankey_from_graph(graph: DiGraph) -> go.Figure:
    """
    Generates a sankey diagram from the passed graph
    NB: subtlety not ro represent to root node.
    """
    fig = go.Figure(data=[go.Sankey(
        arrangement='snap',
        valueformat='.2f',
        node=dict(
            pad=8,
            thickness=1,
            line=dict(width=2),
            label=[graph.nodes[node]['label'] for node in range(len(graph.nodes))],
            color=[graph.nodes[node]['color'] for node in range(len(graph.nodes))],
        ),
        link=dict(
            source=[x[0] for x in graph.edges if x[0] != 0],
            target=[x[1] for x in graph.edges if x[0] != 0],
            value=[graph.edges[(x[0], x[1])]['value'] for x in graph.edges if x[0] != 0],
            color=[graph.edges[(x[0], x[1])]['color'] for x in graph.edges if x[0] != 0],
            label=[graph.edges[(x[0], x[1])]['label'] for x in graph.edges if x[0] != 0],
        ))])
    
    fig.update_layout(
        autosize=True,
        height=800,
    )
    
    return fig
