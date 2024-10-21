"""
Module implementing how to create subplots in plotly
"""
from typing import List

import plotly.graph_objs as go
from plotly.subplots import make_subplots


def subplots(rows: int,
             cols: int,
             shared_xaxes: bool = True,
             row_titles: List[str] | None = None,
             vertical_spacing: float = 0.05) -> go.Figure:
    """
    Function to create subplots
    - rows: number of rows
    - cols: number of columns
    - shared_xaxes: bool to indicate if you want to have a single x axis
    - row_titles: list of titles for each row
    - vertical_spacing: spacing between rows in the figure (0-1)
    """

    return make_subplots(rows=rows,
                         cols=cols,
                         shared_xaxes=shared_xaxes,
                         row_titles=row_titles,
                         vertical_spacing=vertical_spacing)


def subplots_y_axis_labels(fig: go.Figure,
                           text: str,
                           row: int,
                           col: int) -> go.Figure:
    """
    Adds a y-axis label to a specific row and column
    """
    fig.update_yaxes(title_text=text, row=row, col=col)
    return fig
