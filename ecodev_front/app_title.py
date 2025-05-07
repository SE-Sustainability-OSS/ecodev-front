"""
File containing method to retrieve and display the application's name.
"""
import dash_mantine_components as dmc
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


class AppNameConf(BaseSettings):
    """
    Simple authentication configuration class
    """
    app_name: str = ''
    model_config = SettingsConfigDict(env_file='.env')


APP_NAME = AppNameConf().app_name


def app_header_name(app_name: str | None = None, color='white') -> dmc.Title:
    """
    Application name for the header component.
    """
    return dmc.Text(app_name or APP_NAME, c=color, fz=25, fw=700, fs='normal')
