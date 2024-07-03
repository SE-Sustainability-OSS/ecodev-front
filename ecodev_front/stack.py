"""
Module to render a dmc.Stack (main element of a page)
"""
from typing import Any

import dash_mantine_components as dmc


def stack(children: Any,
          id: str | None = None,
          gap: str = 'md',
          align: str = 'stretch') -> dmc.Stack:
    """
    Renders a dmc.Stack component that encapsulates a page
    """
    return dmc.Stack(children=children, align=align, justify='flex-end', gap=gap,
                     id=id)
