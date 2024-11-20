"""
Module implementing select
"""
from typing import Any

import dash_mantine_components as dmc

from ecodev_front.icon import icon


def select(id: str,
           label_text: str | None = None,
           label_id: str | None = '',
           label_color: str = '#A0AEC0',
           value: Any | None = None,
           data: list[str] | None = None,
           persistence: bool = True,
           searchable: bool = True,
           clearable: bool = False,
           allow_deselect: bool = False,
           disabled: bool = False,
           w: str | int = '100%',
           size: str = 'sm',
           left_section: str | None = None,
           stack_id: str | None = '',
           ) -> dmc.Stack:
    """
   Simple select with sensible default parameters
    """

    label = dmc.Text(label_text, c=label_color, id=label_id)

    return dmc.Stack([
        label if label_text else None,
        dmc.Select(
            id=id,
            value=value,
            data=data,
            persistence=persistence,
            searchable=searchable,
            allowDeselect=allow_deselect,
            disabled=disabled,
            clearable=clearable,
            w=w,
            size=size,
            leftSection=icon(left_section) if left_section else None
        ),
    ], gap='xs', w='100%', id=stack_id)
