"""
Module implementing the navbar header components
"""
from typing import List

import dash_mantine_components as dmc
from dash import html
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict

from ecodev_front.constants import MAIN_PAGE_URL
from ecodev_front.login import login

HEADER_DIVIDER = dmc.Divider(orientation='vertical', m=5)


class AppNameConf(BaseSettings):
    """
    Simple authentication configuration class
    """
    app_name: str = ''
    model_config = SettingsConfigDict(env_file='.env')


APP_NAME = AppNameConf().app_name


def app_header(header_logo: dmc.Anchor,
               action_items: List[html.Div],
               user_admin_settings: dmc.Group,
               ) -> dmc.Group:
    """
    Function which determines the display of the various header buttons.
    Only show certain additional buttons to admins or user with owner access to portfolios.
    """
    return dmc.Group(
        children=[header_logo, header_app_pages(action_items), user_admin_settings],
        justify='space-between',
        align='stretch',
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
        },
    )


def header_app_pages(action_items: List[html.Div]) -> dmc.Group:
    """
    Example of how to create / assemble the header for the app specific pages.
    """

    return dmc.Group(
        [x for y in [[x, HEADER_DIVIDER] for x in action_items] for x in y],
        justify='space-around', gap='xl'
    )


def header_logo(app_name: str | None = None,
                logo_path: str = '/assets/logo.png',
                ratio: float = 570 / 128,
                width: str = '120px',
                style: dict[str, str] | None = None) -> dmc.Anchor:
    """
    Application header, composed of an app logo and title components.
    """
    return dmc.Anchor(href=MAIN_PAGE_URL,
                      children=[dmc.Group([app_logo(logo_path, ratio, width, style),
                                           app_title(app_name)])])


def app_logo(logo_path: str = '/assets/logo.png',
             ratio: float = 570 / 128,
             width: str = '120px',
             style: dict[str, str] | None = None
             ) -> dmc.AspectRatio:
    """
    Application logo component.
    """
    style = style or {'margin-left': '10px', 'width': width}
    return dmc.AspectRatio(dmc.Image(src=logo_path), ratio=ratio, style=style)


def app_title(app_name: str | None = None, color='white') -> dmc.Title:
    """
    Application title component.
    """
    return dmc.Title(app_name or APP_NAME, c=color, fz=32)
