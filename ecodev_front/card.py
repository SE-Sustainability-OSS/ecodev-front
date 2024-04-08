"""
Components to create standardised card across apps.
"""
from typing import Dict
from typing import List
from typing import Optional
from typing import Union

import dash_mantine_components as dmc
from dash import html

DEFAULT_STYLE = {'padding': '2%',
                 'position': 'flex',
                 'justifyContent': 'center',
                 'alignItems': 'center',
                 'textAlign': 'center'}


def background_card(children: List,
                    style: Optional[Dict[str, str]] = None,
                    height: Optional[int] = None, className: str = '', card_id: Optional[str] = ''
                    ) -> dmc.Card:
    """
    Returns a formatted dmc.Card
    """
    return dmc.Card(children, radius='md', shadow='sm', p=0, style=style or DEFAULT_STYLE,
                    h=height, className=className, id=card_id)


def overview_card(title: Union[str, dmc.Group, dmc.Tooltip],
                  text: Union[str, float],
                  title_font_size: int = 24,
                  color: str = '#0066A1',
                  text_font_size: int = 24,
                  text_id: Optional[str] = '',
                  title_id: Optional[str] = '',
                  ) -> dmc.Card:
    """
    Renders an overview card
    """

    return dmc.Card([
        card_section(card_title(title, title_font_size, title_id)),
        card_section(
            dmc.Center(
                macro_info(text, color=color, size=text_font_size, text_id=text_id)
            )
        ),
    ], radius='md', shadow='sm')


def card_title(title: str,
               size: int = 24,
               color: str = '#0066A1',
               font: str = 'Averta',
               align: str = 'center',
               title_id: Optional[str] = ''
               ) -> dmc.Text:
    """
    Returns a standardised format of dmc.Text
    """
    return dmc.Text(title, size=size, weight=700, color=color, ff=font, align=align, id=title_id)


def card_section(children: html.Div,
                 graph: bool = False) -> dmc.CardSection:
    """
    Returns a formatted dmc.CardSection from passed dmc.Text
    """
    return dmc.CardSection(dmc.LoadingOverlay(children=children) if graph else children,
                           withBorder=True, inheritPadding=True, py='xs', pl=10)


def macro_info(text: Union[str, float], color: str = '#A0AEC0', size: int = 40,
               text_id: Optional[str] = '') -> dmc.Text:
    """
    Returns a formatted dmc.Text element from a string
    """
    return dmc.Text(text, color=color, fz=size, weight=700, id=text_id)
