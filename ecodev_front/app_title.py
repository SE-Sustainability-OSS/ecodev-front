"""
File containing method to retrieve and display the application's name.
"""
import dash_mantine_components as dmc

from ecodev_front.app_name import APP_NAME


def app_header_name(app_name: str | None = None, color='white') -> dmc.Title:
    """
    Application name for the header component.
    """
    return dmc.Text(app_name or APP_NAME, c=color, fz=25, fw=700, fs='normal')
