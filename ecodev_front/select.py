"""
Module implementing select
"""
from typing import Any

import dash_mantine_components as dmc


def select(id: str,
           label: str,
           value: Any | None = None,
           persistence: bool = True,
           searchable: bool = True,
           clearable: bool = False,
           allow_deselect: bool = False,
           w: str | int = '100%',
           size: str = 'md'
           ) -> dmc.Select:
    """
   Simple select with sensible default parameters
    """
    return dmc.Select(
        id=id,
        label=label,
        value=value,
        data=[],
        persistence=persistence,
        searchable=searchable,
        clearable=clearable,
        allowDeselect=allow_deselect,
        w=w,
        size=size
    )


def select_label(id: str,
                 label: str,
                 value: str | None = None,
                 data: list[str] | None = None,
                 persistence: bool = True,
                 searchable: bool = True,
                 allow_deselect: bool = True,
                 disabled: bool = False,
                 c: str = '#A0AEC0',
                 label_id: str | None = '',
                 stack_id: str | None = '',
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
