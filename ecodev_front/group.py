"""
Module to render dmc.Group elements
"""
from typing import Any

import dash_mantine_components as dmc


def group(children: list[Any],
          grow: bool = True,
          id: str = '',
          justify: str = 'space-around',
          style: dict[str, str] | None = None,
          padding: int = 0
          ) -> dmc.Group:
    """
    Renders a dmc.Group component with the correct formatting
    """
    return dmc.Group(children=children, grow=grow, justify=justify, id=id,
                     style=style or {}, p=padding)
