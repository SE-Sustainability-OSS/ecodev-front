"""
Module implementing the navbar header components
"""
import dash_mantine_components as dmc
from dash import html
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


class AppNameConf(BaseSettings):
    """
    Simple authentication configuration class
    """
    app_name: str = ''
    model_config = SettingsConfigDict(env_file='.env')


APP_NAME = AppNameConf().app_name


def app_logo(logo_path: str = '/assets/logo.png',
             ratio: float = 570 / 128,
             width: str = '120px',
             style: dict[str, str] | None = None
             ) -> dmc.AspectRatio:
    """
    Application logo component.
    """
    style = style or {'margin-left': '10px', 'width': width}
    return dmc.AspectRatio(dmc.Image(src=logo_path),
                           ratio=ratio, style=style)


def app_title(app_name: str | None = None, color='white') -> html.Div:
    """
    Application title component.
    """
    app_name = app_name or APP_NAME
    return html.Div(dmc.Title(app_name, c=color, fz=32))


def app_header(logo: html.Div, title: html.Div) -> dmc.GridCol:
    """
    Application header, composed of an app logo and title components.
    """
    return dmc.GridCol(span='auto',
                       visibleFrom='md',
                       children=[
                           dmc.Anchor(href='/', children=[
                               dmc.Group([logo, title],
                                         justify='space-around',
                                         style={'margin-top': '5px'}),
                           ])
                       ])
