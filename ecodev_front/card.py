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


def background_card(children: List[Union[dmc.CardSection, html.Div]],
                    style: Optional[Dict[str, str]] = None,
                    className: str = '', card_id: Optional[str] = ''
                    ) -> dmc.Card:
    """
    Returns a formatted dmc.Card
    """
    return dmc.Card(children, radius='md', shadow='sm', style=style or DEFAULT_STYLE,
                    className=className, id=card_id)


def overview_card(title: Union[str, dmc.Group, dmc.Tooltip],
                  text: Union[str, float],
                  title_font_size: int = 24,
                  color: str = '#0066A1',
                  text_font_size: int = 16,
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
               size: int = 16,
               title_id: Optional[str] = '',
               color: str = 'white',
               font: str = 'Averta',
               align: str = 'left',
               background_color: str = '#97BDD3'
               ) -> dmc.CardSection:
    """
    Returns a standardised format of dmc.Text
    """
    return card_section(dmc.Text(title, fz=size, fw=900, c=color, ff=font, ta=align, id=title_id,
                                 bg=background_color, p=10))


def card_section(children: Union[html.Div, dmc.Text], graph: bool = False) -> dmc.CardSection:
    """
    Returns a formatted dmc.CardSection from passed dmc.Text
    """
    return dmc.CardSection(children,
                           withBorder=True,
                           style={'height': '100%', 'width': '100%'} if graph else {})


def macro_info(text: Union[str, float], color: str = '#A0AEC0', size: int = 32,
               text_id: Optional[str] = '') -> dmc.Text:
    """
    Returns a formatted dmc.Text element from a string
    """
    return dmc.Text(text, c=color, fz=size, fw=700, id=text_id)
