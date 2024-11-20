from typing import List
from typing import Optional

import plotly.graph_objs as go


def bar_chart(x: List[str | int | float],
              y: List[str | int | float],
              orientation: str = 'v',
              customdata: list[str] | None = None,
              text: str | None = None,
              hovertemplate: str | None = None,
              colors: list[str] | None = None,
              textposition: str = 'inside',
              name: Optional[str] = '',
              legendgroup: Optional[str] = '') -> go.Bar:
    """
    Function to render a bar chart
     - x: list of x-value which will also be shown as x-axis labels
     - y: numerical values that will be aggregated
     - orientation: ('h'|'v') determines whether the chart will be displayed horizontally or
     vertically
     - customdata: list of str that represent a text we want to use in the hovertemplate
     - text: list of str that will be displayed in the graph
     - hovertemplate: str that must be formatted like html, that will show when you hover on the
     graph
     - colors: list of custom colors to be applied to the pie chart. Plotly default colors will
     be applied if not filled in
     - textposition: determines where the text should be placed,
     - name: str that will be displayed in the legend
     - legendgroup: str when you want to group legend items
    """
    return go.Bar(
        x=x,
        y=y,
        orientation=orientation,
        customdata=customdata,
        name=name,
        legendgroup=legendgroup,
        text=text,
        textposition=textposition,
        marker={'color': colors},
        hovertemplate=hovertemplate,
    )
