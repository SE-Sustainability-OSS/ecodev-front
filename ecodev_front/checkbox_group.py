"""
Module implementing a checkbox group select component
"""
from typing import Any

import dash_mantine_components as dmc

from ecodev_front.constants import INDEX
from ecodev_front.constants import LABEL
from ecodev_front.constants import TYPE
from ecodev_front.constants import VALUE
from ecodev_front.ids import CHECKBOX_GROUP
from ecodev_front.text import label_text


def checkbox_group(id: str | dict,
                   data: list[dict],
                   value: list[str] | None = None,
                   label: str = '',
                   color: str = '#0066a1',
                   size: str = 'sm',
                   gap: str = 'xs',
                   label_kwargs: dict = {},
                   **kwargs: Any
                   ) -> dmc.CheckboxGroup:
    """
    Renders a checkbox group component.

    data items must follow the {VALUE: ..., LABEL: ...} format.
    """
    checkboxes = dmc.Stack(
        [dmc.Checkbox(label=item[LABEL], value=item[VALUE], size=size, color=color)
         for item in data],
        gap=gap,
    )
    resolved_id = id if isinstance(id, dict) else {TYPE: CHECKBOX_GROUP, INDEX: id}
    group = dmc.CheckboxGroup(
        id=resolved_id,
        value=value if value is not None else [item[VALUE] for item in data],
        children=checkboxes,
        **kwargs
    )
    if not label:
        return group

    return dmc.Stack([label_text(label, **label_kwargs), group], gap='0px')
