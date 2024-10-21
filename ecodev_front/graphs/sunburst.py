from typing import Dict
from typing import List
from typing import Tuple

import plotly.graph_objs as go

from ecodev_front import VALUE
from ecodev_front.display_utils import number_formatting


def sunburst(ids: List[str],
             labels: List[str],
             parents: List[str],
             values: List[float],
             hovertemplate: str | None = None,
             customdata: list[str] | None = None,
             textinfo: str = 'label+percent entry',
             branchvalues: str = 'total',
             name: str = '',
             colors: List[str] | None = None,
             insidetextorientation: str = 'horizontal'
             ) -> go.Sunburst:
    """
    Function to render a sunburst
     - ids: a list of unique ids
     - labels: the text that will appear on the graph for each section
     - parents: a list of ids of each parent node
     - values: a list of numerical values
     - hovertemplate: str that must be formatted like html, that will show when you hover on the
     graph
     - customdata: list of str that represent a text we want to use in the hovertemplate
     - textinfo: the format of the string that will be displayed on the graph
     - mode: what kind of points will be displayed
     - color: custom color to be applied to the pie chart. Plotly default colors will
     be applied if not filled in
     - textposition: determines where the text should be placed,
     - branchvalues: whether you want the sunburst graph to be completed 360 or not (the sum of
     children values must be equal to the parent value)
     - name: str that will be displayed in the legend
     - colors: list of custom colors to be applied to the pie chart. Plotly default colors will
     be applied if not filled in
     - insidetextorientation: str to indicate how the text will be displayed
    """
    return go.Sunburst(ids=ids,
                       labels=labels,
                       parents=parents,
                       values=values,
                       hovertemplate=hovertemplate,
                       customdata=customdata,
                       textinfo=textinfo,
                       branchvalues=branchvalues,
                       name=name,
                       marker={'colors': colors or []},
                       insidetextorientation=insidetextorientation)


def get_formatted_data_sunburst(data: Dict,
                                level_1_col: str,
                                level_2_col: str,
                                value_col: str = VALUE,
                                unit: str | None = ''
                                ) -> Tuple[List, List, List, List]:
    """
    Returns four lists which will be used in the Sunburst chart
      - ids: a list of unique ids
      - labels: the text that will appear on the graph for each section
      - parents: a list of ids of each parent node
      - values: a list of numerical values
    Arguments:
        - data: a dict
        - level_1_col: the column name for the first level of the sunburst chart
        - level_2_col: the column name for the second level of the sunburst chart
        - value_col: the column name for the numerical value (default is VALUE)
        - unit: the unit for the numerical value (default is '')
    """
    if not data:
        return [], [], [], []

    total = sum(x[value_col] for x in data.values())
    ids = [f'{number_formatting(total)} {unit}']
    labels = [f'{number_formatting(total)} {unit}']
    parents = ['']
    values = [total]

    total_values = {level_1: 0 for level_1 in {x[level_1_col] for x in data.values()}}
    for x in data.values():
        total_values[x[level_1_col]] += x[VALUE]

    for key, value in total_values.items():
        ids.append(key or 'None')
        labels.append(key or 'None')
        parents.append(f'{number_formatting(total)} {unit}')
        values.append(value)

    for categories in data.values():
        ids.append(f'{categories[level_1_col]}_{categories[level_2_col]}')
        labels.append(categories[level_2_col] or 'None')
        parents.append(categories[level_1_col] or 'None')
        values.append(categories[value_col])

    return ids, labels, parents, values
