"""
Module to render a dmc.Stack (main element of a page)
"""
from typing import Any
from typing import Optional

import dash_mantine_components as dmc


def stack(children: Any,
          stack_id: Optional[str] = '',
          gap: str = 'md',
          align: str = 'stretch') -> dmc.Stack:
    """
    Renders a dmc.Stack component that encapsulates a page
    """
    return dmc.Stack(children=children, align=align, justify='flex-end', gap=gap,
                     id=stack_id)
