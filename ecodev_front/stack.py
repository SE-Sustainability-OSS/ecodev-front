"""
Module to render a dmc.Stack (main element of a page)
"""
from typing import Any

import dash_mantine_components as dmc


def stack(children: Any,
          id: str = '',
          gap: str | int = 'md',
          width: int | str = '100%',
          align: str = 'stretch',
          justify: str = 'flex-end',
          style: dict | None = None,
          padding: int = 0
          ) -> dmc.Stack:
    """
    Renders a dmc.Stack component that encapsulates a page
    """
    return dmc.Stack(children=children, align=align, justify=justify, gap=gap, id=id,
                     w=width, style=style, p=padding)
