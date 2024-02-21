"""
Components to create standardised card across apps.
"""
from typing import Dict
from typing import List
from typing import Optional

import dash_mantine_components as dmc
from dash import html

DEFAULT_STYLE = {'padding': '2%',
                 'position': 'flex',
                 'justifyContent': 'center',
                 'alignItems': 'center',
                 'textAlign': 'center'}


def background_card(children: List[dmc.CardSection],
                    style: Optional[Dict[str, str]] = None) -> dmc.Card:
    """
    Returns a formatted dmc.Card
    """
    return dmc.Card(children, radius='md', shadow='sm', p=0, style=style or DEFAULT_STYLE)


def card_title(title: str,
               size: int = 24,
               color: str = '#0066A1',
               font: str = 'Averta',
               align: str = 'center',
               ) -> dmc.Text:
    """
    Returns a standardised format of dmc.Text
    """
    return dmc.Text(title, size=size, weight=700, color=color, ff=font, align=align)


def card_section(children: html.Div) -> dmc.CardSection:
    """
    Returns a formatted dmc.CardSection from passed dmc.Text
    """
    return dmc.CardSection(children, withBorder=True, inheritPadding=True, py='xs', pl=10)


def macro_info(text: str, color: str = '#A0AEC0', size: int = 40) -> dmc.Text:
    """
    Returns a formatted dmc.Text element from a string
    """
    return dmc.Text(text, color=color, style={'fontSize': size}, weight=700)
