"""
Module containing the app footer component style
"""
from typing import Dict
from typing import Union

import dash_mantine_components as dmc
from dash import dcc
from dash import html

from ecodev_front.constants import COMM_CHANNEL_URL
from ecodev_front.constants import FEEDBACK_URL
from ecodev_front.ids import FOOTER


def app_footer() -> dmc.Group:
    """
    Example of implementation of an app's footer.
    """
    return _footer(
        dmc.Group(
            [
                dcc.Markdown(
                    f'##### Questions? Bugs? [Contact us here]({COMM_CHANNEL_URL})',
                    link_target='_blank',
                ),
                dcc.Markdown(
                    f'##### Any [comments or feedback]({FEEDBACK_URL}) is welcome!',
                    link_target='_blank',
                ),
            ]
        )
    )


def _footer(
    children: html.Div,
    color: str = '#0066A1',
    height: str = '4vh',
    display: str = 'flex',
) -> html.Div:
    """
    Main app footer
    """
    return html.Div(children, id=FOOTER, style=footer_style(color, height, display))


def footer_style(
    color: str = '#0066A1', height: str = '5vh', display: str = 'flex'
) -> Dict[str, Union[str, int]]:
    """
    Main app footer style
    """
    return {
        'position': 'fixed',
        'bottom': 0,
        'height': height,
        'width': '100vw',
        'paddingBottom': '10px',
        'backgroundColor': color,
        'color': 'white',
        'display': display,
        'textAlign': 'center',
        'alignContent': 'center',
        'justifyContent': 'center',
    }
