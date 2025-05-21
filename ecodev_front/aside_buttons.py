"""
Renders a collapsible aside open & close buttons
"""
import dash_mantine_components as dmc
from dash import html
from dash_iconify import DashIconify
from ecodev_core import logger_get


log = logger_get(__name__)

SHOW = {'display': 'block'}
HIDE = {'display': 'none'}

OPEN_ASIDE_BTN_ID = 'open-aside-btn-id'
CLOSE_ASIDE_BTN_ID = 'close-aside-btn-id'


def open_aside_button() -> dmc.Affix:
    """
    Returns an aside open button, at the edge of the right hand side of the screen.
    """
    return dmc.Affix(
        dmc.ActionIcon(
            DashIconify(icon='fluent:filter-16-regular', width=25),
            id=OPEN_ASIDE_BTN_ID,
            size=40,
            variant='default',
            c='white',
            bg='#0066A1',
            style=HIDE,
        ),
        position={'top': 63, 'right': -5},
        zIndex=91,
    )


def close_aside_button(aside_width: str = '272px') -> dmc.Affix:
    """
    Returns an aside close button, at edge of where the aside extends.
    """
    return dmc.Affix(
        dmc.ActionIcon(
            DashIconify(icon='oui:cross', width=25),
            id=CLOSE_ASIDE_BTN_ID,
            size=40,
            variant='default',
            c='white',
            bg='#0066A1',
            style=HIDE,
        ),
        position={'top': 63, 'right': aside_width},
        zIndex=89,
    )


def aside_buttons(aside_width: str = '272px') -> html.Div:
    """
    Renders the aside buttons on a page. Must be present on the layout of every page
    containing a collapsible aside.
    """
    return html.Div([open_aside_button(), close_aside_button(aside_width)])
