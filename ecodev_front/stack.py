"""
Module to render a dmc.Stack (main element of a page)
"""
from typing import List
from typing import Optional
from typing import Union

import dash_mantine_components as dmc
from dash import html


def stack(children: List[Union[dmc.Group, dmc.Card, dmc.Center, html.Div]],
          stack_id: Optional[str] = '') -> dmc.Stack:
    """
    Renders a dmc.Stack component that encapsulates a page
    """
    return dmc.Stack(children=children, align='stretch', justify='flex-end', id=stack_id)
