"""
Module implementing how to render an Accordion
"""
from typing import Any

import dash_mantine_components as dmc
from dash import html

from ecodev_front.icon import dash_icon


def accordion(children: Any,
              multiple: bool = True,
              radius: int = 10,
              variant: str = 'default',
              width: int | str = '100%'):
    """
    Returns an accordion component
    """
    return dmc.Accordion(
        children=children,
        multiple=multiple,
        radius=radius,
        variant=variant,
        width=width
    )


def accordion_item(id: str,
                   icon: str,
                   color: str,
                   text: str,
                   num_securities: int,
                   content: Any):
    """
    Returns an accordion item
    """
    return dmc.AccordionItem(id=id, value=id, w='100%',
                             children=[
                                 dmc.AccordionControl(
                                     dmc.Group([
                                         dmc.Group(
                                             [dash_icon(icon, width=24, color=color),
                                              dmc.Text(html.Span(text,
                                                                 style={'color': 'gray',
                                                                        'fontWeight': 650}))],
                                             justify='left', gap='xs'),
                                         dmc.Kbd(num_securities, fz=14, c=color, mr=10),
                                     ], justify='space-between')),
                                 dmc.AccordionPanel(content)
                             ])
