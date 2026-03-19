"""
Module implementing multi select
"""
from typing import Any

import dash_mantine_components as dmc

from ecodev_front.icon import dash_icon


def multi_select(id: str | dict,
                 label_text: str | None = None,
                 label_id: str | None = '',
                 label_color: str = '#A0AEC0',
                 value: list[Any] | None = None,
                 data: list[str] | None = None,
                 persistence: bool = True,
                 searchable: bool = True,
                 clearable: bool = True,
                 disabled: bool = False,
                 w: str | int = '100%',
                 size: str = 'sm',
                 left_section: str | None = None,
                 stack_id: str | None = '',
                 placeholder: str | None = None,
                 ) -> dmc.Stack | dmc.MultiSelect:
    """
    Multi select with sensible default parameters
    """
    content = dmc.MultiSelect(
        id=id,
        value=value if value is not None else [],
        data=data,
        persistence=persistence,
        searchable=searchable,
        clearable=clearable,
        disabled=disabled,
        w=w,
        size=size,
        leftSection=dash_icon(left_section) if left_section else None,
        placeholder=placeholder,
    )

    if not label_text:
        return content

    return dmc.Stack([
        dmc.Text(label_text, c=label_color, id=label_id),
        content
    ], gap='xs', w='100%', id=stack_id)
