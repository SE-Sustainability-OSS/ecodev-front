"""
Module implementing select
"""
from typing import Any
from typing import List
from typing import Optional
from typing import Union

import dash_mantine_components as dmc


def select(select_id: str,
           label: str,
           value: Optional[Any] = None,
           persistence: bool = True,
           searchable: bool = True,
           w: Union[str, int] = '100%',
           ) -> dmc.Select:
    """
    Renders a formatted html.Div with content at the center
    Useful to center plotly graphs
    """
    return dmc.Select(
        id=select_id,
        label=label,
        value=value,
        data=[],
        persistence=persistence,
        searchable=searchable,
        w=w
    )


def select_label(id: str,
                 label: str,
                 value: Optional[str] = None,
                 data: Optional[List[str]] = None,
                 persistence: bool = True,
                 searchable: bool = True,
                 allow_deselect: bool = True,
                 disabled: bool = False,
                 c: str = '#A0AEC0',
                 label_id: Optional[str] = '',
                 stack_id: Optional[str] = '',
                 ) -> dmc.Stack:
    """
    Renders a select with a stylized label
    """
    return dmc.Stack([
        dmc.Text(label, c=c, id=label_id),
        dmc.Select(
            id=id,
            value=value,
            data=data,
            persistence=persistence,
            searchable=searchable,
            allowDeselect=allow_deselect,
            disabled=disabled
        ),
    ], gap='xs', w='100%', id=stack_id)
