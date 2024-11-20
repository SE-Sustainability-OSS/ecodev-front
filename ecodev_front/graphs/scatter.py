"""
Module to render a go.Scatter plotly graph
"""
from typing import Dict
from typing import List

import plotly.graph_objs as go


def scatter(x: List[str | int | float],
            y: List[int | float],
            text: List | None = None,
            textfont: Dict | None = None,
            mode: str = 'lines+text',
            color: str | None = None,
            line_width: float = 1,
            fill: str | None = None,
            textposition: str = 'top center',
            customdata: list[str] | None = None,
            hovertemplate: str | None = None,
            name: str = '',
            legendgroup: int = 1,
            stackgroup: str = '',
            show_legend: bool = True) -> go.Scatter:
    """
    Function to render a scatter plot
     - x: information that will be at the bottom of the graph (can be dates, aggregations, etc...)
     - y: numerical values that will be aggregated
     - text: list of strings to be displayed on the scatter points
     - textfont: dictionary to customize the font of the text
     - mode: what kind of points will be displayed
     - color: custom color to be applied to the pie chart. Plotly default colors will
     be applied if not filled in
     - line_width: width of the line connecting the data points
     - fill: (tonexty) fills the area under the curve
     - textposition: determines where the text should be placed,
     - customdata: list of str that represent a text we want to use in the hovertemplate
     - hovertemplate: str that must be formatted like html, that will show when you hover on the
     graph
     - name: str that will be displayed in the legend
     - legendgroup: str when you want to group legend items
     - stackgroup: str to indicate which lines you want to stack together
     - show_legend: bool to show or hide the legend for this trace
    """

    return go.Scatter(x=x,
                      y=y,
                      text=text,
                      textfont=textfont or {},
                      mode=mode,
                      line={'color': color, 'width': line_width},
                      fill=fill,
                      textposition=textposition,
                      customdata=customdata,
                      hovertemplate=hovertemplate,
                      name=name,
                      legendgroup=legendgroup,
                      stackgroup=stackgroup,
                      showlegend=show_legend)
