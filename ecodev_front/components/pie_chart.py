from typing import List
from typing import Union

import plotly.graph_objects as go


def pie_chart(labels: List[str],
              values: List[Union[int, float]],
              customdata: List[str] = None,
              hovertemplate: List[str] = None,
              colors: List[str] = None,
              text_threshold: float = 0.1,
              annotation_text: str = None
              ):
    """
    Function to render a pie chart
     - labels: column on which we want to perform an aggregation
     - values: numerical values that will be aggregated
     - customdata: list of str that represent a text we want to use in the hovertemplate
     - hovertemplate: str that must be formatted like html, that will show when you hover on the
     graph
     - colors: list of custom colors to be applied to the pie chart. Plotly default colors will
     be applied if not filled in
     - text_threshold: float between 0 and 1, that controls the minimum threshold in terms of
     percentage of the total under which category labels will be shown. The higher the threshold,
     the less categories will be shown (only the biggest one),
     - annotation_text: text that will be displayed at the center of the pie chart
    """

    annotation = [{'text': annotation_text, 'font': {'size': 18}, 'showarrow': False,
                   }] if annotation_text else []

    return go.Figure(
        go.Pie(
            labels=labels,
            values=values,
            customdata=customdata,
            hovertemplate=hovertemplate,
            marker={'colors': colors},
            textinfo='percent+label',
            texttemplate='%{label} <br>%{percent:.0%}',
            textposition=['none' if value / sum(values) < text_threshold else
                          'auto' for value in values],
            hole=0.4,
            sort=False,
            name='',
        ),
        layout=go.Layout(
            annotations=annotation,
            uniformtext={'minsize': 14, 'mode': 'hide'},
            font={'family': 'Averta', 'size': 14},
            showlegend=False,
        ),
    )
