"""
Module implementing the app header components
"""
import dash_mantine_components as dmc
from dash import html

from ecodev_front.app_logo import app_logo
from ecodev_front.app_title import app_header_name
from ecodev_front.login import login

HEADER_DIVIDER = dmc.Divider(orientation='vertical', m=5)


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
