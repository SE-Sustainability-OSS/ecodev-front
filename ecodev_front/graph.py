"""
Dash app component to display a graph with correct sizing / padding.
"""
import plotly.graph_objects as go
from dash import dcc


def graph_box(fig: go.Figure) -> dcc.Graph:
    """
    Helper component to format a plotly figure with correct sizing & padding.
    """
    fig.update_layout(
        margin={'t': 10, 'l': 10, 'b': 10, 'r': 10},
    )
    return dcc.Graph(figure=fig, style={'width': '90%', 'height': '90%'})