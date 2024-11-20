import plotly.graph_objects as go


def pie_chart(labels: list[str],
              values: list[int | float],
              customdata: list[str] | None = None,
              text: list[str] | None = None,
              hovertemplate: str | None = None,
              colors: list[str] | None = None,
              text_threshold: float = 0.1,
              text_info: str = 'label+percent',
              texttemplate: str = ''
              ) -> go.Pie:
    """
    Function to render a pie chart
     - labels: column on which we want to perform an aggregation
     - values: numerical values that will be aggregated
     - customdata: list of str that represent a text we want to use in the hovertemplate
     - text: list of str that will be displayed in the graph
     - hovertemplate: str that must be formatted like html, that will show when you hover on the
     graph
     - colors: list of custom colors to be applied to the pie chart. Plotly default colors will
     be applied if not filled in
     - text_threshold: float between 0 and 1, that controls the minimum threshold in terms of
     percentage of the total under which category labels will be shown. The higher the threshold,
     the less categories will be shown (only the biggest one),
    """

    return go.Pie(
        labels=labels,
        values=values,
        customdata=customdata,
        text=text,
        hovertemplate=hovertemplate,
        marker={'colors': colors},
        textinfo=text_info,
        texttemplate=texttemplate,
        textposition=['none' if value / sum(values) < text_threshold else
                      'auto' for value in values],
        hole=0.4,
        sort=False,
        name='',
    )
