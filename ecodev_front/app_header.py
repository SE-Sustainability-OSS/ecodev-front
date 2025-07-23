"""
Module implementing the app header components
"""
import dash_mantine_components as dmc
from dash import html
from ecodev_core import SETTINGS

from ecodev_front.app_logo import app_logo
from ecodev_front.app_title import app_header_name
from ecodev_front.constants import LOGIN_PAGE_URL
from ecodev_front.constants import MAIN_PAGE_URL
from ecodev_front.documentation import documentation_icon_link
from ecodev_front.icon import dash_icon
from ecodev_front.ids import HOME_BUTTON_ID
from ecodev_front.ids import LOGOUT_BTN_ID
from ecodev_front.login import login
from ecodev_front.nav_items import action_item

HEADER_DIVIDER = dmc.Divider(orientation='vertical', color='gray.2', mt=10, mb=10, ml=30, mr=30)

HOME_ACTION_ICON = dmc.ActionIcon([
    dash_icon('mdi:chevron-left', color='white', width=80),
    dash_icon('ic:round-home', color='white', width=80)
], variant='transparent', size='xl', id=HOME_BUTTON_ID, ml=5, mr=5)

LOGOUT_BUTTON = action_item(
    id=LOGOUT_BTN_ID, label='LOGOUT', icon='ic:baseline-logout', href=LOGIN_PAGE_URL
)


def display_app_header(pathname: str,
                       module_action_items: dmc.Group,
                       app_name: str | None = None) -> dmc.Group:
    """
    Function which determines the display of the app header. By default, we always show the home
    and logout buttons as well as the app name. The list of modules that can be displayed need to
    be parametrized in each app.
    """
    is_main_page = pathname == MAIN_PAGE_URL
    return dmc.Group(justify='space-between',
                     children=[
                         dmc.Group([
                             None if is_main_page else HOME_ACTION_ICON,
                             app_header_name(app_name or SETTINGS.app_name)
                         ], mt='5px', ml='1%' if is_main_page else 5, align='center'),
                         module_action_items,
                         dmc.Group([
                             documentation_icon_link(icon_color='white'),
                             LOGOUT_BUTTON
                         ])
                     ])


def app_header(header_logo: dmc.Anchor,
               action_items: list[html.Div],
               user_admin_settings: dmc.Group,
               ) -> dmc.Group:
    """
    Function which determines the display of the various header buttons.
    Only show certain additional buttons to admins or user with owner access to portfolios.
    """
    return dmc.Group(
        children=[app_logo(), app_header_name(), header_app_pages(
            action_items), user_admin_settings],
        justify='space-between',
        align='center',
        style={
            'backgroundColor': '#0066A1',
            'color': 'white',
        }, mt=5)


def header_login(app_header: dmc.Anchor) -> dmc.Group:
    """
    Renders a header with login components (username and password input fields)
    """
    return dmc.Group(
        children=[app_header, login()],
        justify='space-between',
        align='stretch',
        style={
            'backgroundColor': '#0066A1',
            'color': 'white',
        }, mt=5
    )


def header_app_pages(action_items: list[html.Div]) -> dmc.Group:
    """
    Example of how to create / assemble the header for the app specific pages.
    """
    return dmc.Group(
        [x for y in [[x, HEADER_DIVIDER] for x in action_items] for x in y],
        justify='space-around', gap='xl'
    )
