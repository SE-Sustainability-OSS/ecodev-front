"""
Module to render dmc.Group elements
"""
from typing import List

import dash_mantine_components as dmc


def group(children: List,
          grow: bool = True,
          id: str = '',
          justify: str = 'space-around') -> dmc.Group:
    """
    Renders a dmc.Group component with the correct formatting
    """
    return dmc.Group(children=children, grow=grow, justify=justify, id=id)
