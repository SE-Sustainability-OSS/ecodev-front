"""
Module containing the app footer component style
"""
from dash import html

from ecodev_front.ids import FOOTER_ID


def app_footer(children: html.Div,
               color: str = '#0066A1',
               height: str = '4vh',
               display: str = 'flex',
               ) -> html.Div:
    """
    Main app footer
    """
    return html.Div(children, id=FOOTER_ID, style=footer_style(color, height, display))


def footer_style(color: str = '#0066A1',
                 height: str = '5vh',
                 display: str = 'flex'
                 ) -> dict[str, str | int]:
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
