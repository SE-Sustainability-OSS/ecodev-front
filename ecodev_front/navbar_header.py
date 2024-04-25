"""
Module implementing the navbar header components
"""
import os

import dash_mantine_components as dmc
from dash import html


def app_logo(logo_path: str = '/assets/logo.png',
             ratio: float = 570/128,
             width: str = '120px',
             style: dict[str, str] | None = None):
    """
    Application logo component.
    """
    style = style or {'margin-left': '10px', 'margin-top': '10px', 'width': width}
    return dmc.AspectRatio(dmc.Image(src=logo_path),
                           ratio=ratio, style=style)


def app_title(app_name: str | None = None, color='white'):
    """
    Application title component.
    """
    app_name = app_name or os.getenv('app_name')
    return html.Div(dmc.Title(os.getenv('app_name'), c=color, fz=32))


logo = app_logo()
title = app_title()


def navbar_header(app_logo: html.Div = logo,
                  app_title: html.Div = title):
    """
    Application header, composed of an app logo and title components.
    """
    return dmc.GridCol(span='auto',
                       visibleFrom='md',
                       children=[
                           dmc.Anchor(href='/', children=[
                               dmc.Group([app_logo, app_title],
                                         justify='space-around'),
                           ])
                       ])
