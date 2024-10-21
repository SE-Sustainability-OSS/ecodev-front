"""
Component which allows document download
"""
import dash_mantine_components as dmc
from dash import dcc
from dash_iconify import DashIconify

from ecodev_front.button import button


def download_button(id: str,
                    text: str,
                    icon: DashIconify,
                    download_id: str,
                    color: str = 'default-color',
                    ) -> dmc.Stack:
    """
    Returns a Div comprised of a button fully customisable and a dcc.Download component
    """
    return dmc.Stack(
        [
            button(id, text, icon, color),
            dcc.Download(id=download_id)
        ],
    )
