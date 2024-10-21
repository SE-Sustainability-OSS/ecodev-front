"""
Module to render a go.Scatter plotly graph
"""
from typing import List

import plotly.graph_objs as go


def scatter(x: List[str | int | float],
            y: List[int | float],
            text: List[str] | None = None,
            mode: str = 'lines+text',
            color: str | None = None,
            fill: str | None = None,
            textposition: str = 'top center',
            hovertemplate: str | None = None,
            name: str = '',
            legendgroup: int = 1,
            stackgroup: str = '') -> go.Scatter:
    """
    Function to render a scatter plot
     - x: information that will be at the bottom of the graph (can be dates, aggregations, etc...)
     - y: numerical values that will be aggregated
     - text: list of strings to be displayed on the scatter points
     - mode: what kind of points will be displayed
     - color: custom color to be applied to the pie chart. Plotly default colors will
     be applied if not filled in
     - fill: (tonexty) fills the area under the curve
     - textposition: determines where the text should be placed,
     - hovertemplate: str that must be formatted like html, that will show when you hover on the
     graph
     - name: str that will be displayed in the legend
     - legendgroup: str when you want to group legend items
     - stackgroup: str to indicate which lines you want to stack together
    """

    return go.Scatter(x=x,
                      y=y,
                      text=text,
                      mode=mode,
                      line={'color': color},
                      fill=fill,
                      textposition=textposition,
                      hovertemplate=hovertemplate,
                      name=name,
                      legendgroup=legendgroup,
                      stackgroup=stackgroup)
