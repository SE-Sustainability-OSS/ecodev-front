"""
Module implementing select
"""
from typing import Any

import dash_mantine_components as dmc

from ecodev_front.icon import dash_icon


def select(id: str | dict,
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
           placeholder: str | None = None,
           ) -> dmc.Stack | dmc.Select:
    """
    Simple select with sensible default parameters
    """
    content = dmc.Select(
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
        leftSection=dash_icon(left_section) if left_section else None,
        placeholder=placeholder
    )

    if not label_text:
        return content

    return dmc.Stack([
        dmc.Text(label_text, c=label_color, id=label_id),
        content
    ], gap='xs', w='100%', id=stack_id)
