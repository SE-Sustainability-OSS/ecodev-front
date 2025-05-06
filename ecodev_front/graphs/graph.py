"""
Dash app component to display a graph with correct sizing / padding.
"""
import plotly.graph_objects as go
from dash import dcc

from ecodev_front.graphs.plotly_tools import PLOTLY_TOOLS


def graph_box(fig: go.Figure, id: str = '',
              height: int | str = '100%',
              width: int | str = '100%') -> dcc.Graph:
    """
    Helper component to format a plotly figure with correct sizing & padding.
    """
    return dcc.Graph(figure=fig,
                     config={'modeBarButtonsToRemove': PLOTLY_TOOLS, 'displaylogo': False},
                     style={'height': height, 'width': width}, id=id)
