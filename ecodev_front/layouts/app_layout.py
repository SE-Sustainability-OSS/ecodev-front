"""
Base app component, utilising dmc.AppShell.
"""
import dash
import dash_mantine_components as dmc
from dash import dcc

from ecodev_front.components.footer import app_footer
from ecodev_front.ids import LEFT_ASIDE_ID
from ecodev_front.ids import NAVBAR_ID
from ecodev_front.ids import RIGHT_ASIDE_ID
from ecodev_front.ids import TOKEN
from ecodev_front.ids import URL


def dash_base_layout(stores: list[tuple[str, str]],
                     colors: dict[str, list[str]] | None = None) -> dmc.MantineProvider:
    """
    Returns a base layout for any Dash application
    """
    return dmc.MantineProvider(
        forceColorScheme='light',
        theme={'colors': colors} if colors else None,
        children=dmc.AppShell(
            [
                dcc.Location(id=URL, refresh=True),
                dcc.Store(id=TOKEN, data={TOKEN: None}, storage_type='local'),
                *[dcc.Store(id=store_id, storage_type=storage_type)
                  for store_id, storage_type in stores],
                dmc.AppShellHeader(id=NAVBAR_ID, style={'background-color': '#0066A1'}, zIndex=100),
                dmc.AppShellAside(id=RIGHT_ASIDE_ID, zIndex=100),
                dmc.AppShellNavbar(id=LEFT_ASIDE_ID, zIndex=100),
                dmc.AppShellMain(dash.page_container, style={'margin-top': '2%'}),
                dmc.AppShellFooter(app_footer(), zIndex=100),
            ],
            style={'padding-inline': '0px', 'background-color': '#f2f2f2'},
            header={'height': 55},
            footer={'height': 40},
            navbar={'width': 300,
                    'breakpoint': 'xl',
                    'collapsed': {'desktop': False, 'mobile': True},
                    },
            aside={'width': 300,
                   'breakpoint': 'xl',
                   'collapsed': {'desktop': False, 'mobile': True},
                   },
        )
    )
