"""
Module implementing the navbar header components
"""
import os
from typing import Dict
from typing import Optional

import dash_mantine_components as dmc
from dash import html


def app_logo(logo_path: str = '/assets/logo.png',
             maw: int = 160,
             style: Optional[Dict[str, str]] = None):
    """
    Application logo component.
    """
    style = style or {'margin-left': '10px',
                      'margin-top': '7px',
                      'margin-bottom': '7px'}
    return dmc.Image(src=logo_path, maw=maw, style=style)


def app_title(app_name: Optional[str] = None, color='white'):
    """
    Application title component.
    """
    app_name = app_name or os.getenv('app_name')
    return html.Div(dmc.Title(os.getenv('app_name'), color=color))


logo = app_logo()
title = app_title()


def navbar_header(app_logo: html.Div = logo,
                  app_title: html.Div = title,
                  spacing: int = 50):
    """
    Application header, composed of an app logo and title components.
    """
    return dmc.Col(span=4,
                   children=[
                       dmc.Group([app_logo,
                                  dmc.Space(w=spacing),
                                  app_title
                                  ])
                   ])
