"""
Module to render dmc.Group elements
"""
from typing import List
from typing import Optional

import dash_mantine_components as dmc


def group(children: List,
          className: Optional[str] = '',
          grow: bool = True,
          group_id: str = '') -> dmc.Group:
    """
    Renders a dmc.Group component with the correct formatting
    """
    return dmc.Group(children=children, grow=grow, pos='center',
                     justify='center', className=className, id=group_id)
