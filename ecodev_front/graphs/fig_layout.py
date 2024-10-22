from typing import Dict

import plotly.graph_objs as go

from ecodev_front.graphs.legend_position import BOTTOM_LEGEND


def apply_fig_layout(fig: go.Figure,
                     title: str | None = None,
                     barmode: str = 'stack',
                     annotation_text: str | None = None,
                     show_legend: bool = True,
                     legend: Dict = BOTTOM_LEGEND,
                     margin_left: int = 0,
                     margin_right: int = 0,
                     margin_top: int = 0,
                     margin_bottom: int = 0,
                     minsize: int | None = None,
                     hovermode: str = 'x'
                     ):
    """
    Function to configure layout options on a plotly figure
    - fig: the figure on which you want to apply the layout
    - title: str that will be the title of the graph
    - barmode: determines how bars are displayed in a grouped bar chart
    - annotation_text: text that will be displayed at the center of the pie chart
    - show_legend: bool, whether to display the legend or not (default: False)
    - legend: controls the orientation of the legend
    - margins: control the spacing on the sides of the graph
    - minsize: minimum font size (elements under this size would not be displayed)
    """

    annotation = [{'text': annotation_text, 'font': {'size': 18}, 'showarrow': False,
                   }] if annotation_text else []

    fig.update_layout(title={'text': title},
                      barmode=barmode,
                      annotations=annotation,
                      uniformtext={'minsize': minsize, 'mode': 'hide'},
                      font={'family': 'Averta', 'size': 14},
                      showlegend=show_legend,
                      legend=legend,
                      hovermode=hovermode,
                      margin={'l': margin_left, 'r': margin_right,
                              't': margin_top, 'b': margin_bottom})
