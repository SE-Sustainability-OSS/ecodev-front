"""
Module containing formatted divs.
"""
from typing import Any

from dash import html


def centered_div(children: Any) -> html.Div:
    """
    Renders a formatted html.Div with content at the center
    Useful to center plotly graphs
    """
    return html.Div(children=children, style={'height': '100%',
                                              'width': '100%',
                                              'display': 'flex',
                                              'justifyContent': 'center',
                                              'alignItems': 'center'})
