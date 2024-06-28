"""
Base app component, utilising dmc.AppShell.
"""
import dash
import dash_mantine_components as dmc
from dash import dcc

from ecodev_front.ids import FOOTER_ID
from ecodev_front.ids import LEFT_ASIDE_ID
from ecodev_front.ids import NAVBAR_ID
from ecodev_front.ids import RIGHT_ASIDE_ID
from ecodev_front.ids import TOKEN
from ecodev_front.ids import URL


def dash_base_layout(stores: list[tuple[str, str]],
                     colors: dict[str, list[str]] | None = None,
                     header_height: int = 55,
                     footer_height: int = 40,
                     navbar_width: int = 300,
                     aside_width: int = 300) -> dmc.MantineProvider:
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
                dmc.AppShellHeader(id=NAVBAR_ID, style={'background-color': '#0066A1'},
                                   zIndex=100, children=[]),
                dmc.AppShellNavbar(
                    id=LEFT_ASIDE_ID,
                    children=[],
                    zIndex=90,
                    style={'display': 'none'},
                    withBorder=True, visibleFrom='md'),

                dmc.AppShellMain(dash.page_container, style={'margin-top': '2%',
                                                             'justifyContent': 'center',
                                                             'display': 'flex'}),
                dmc.AppShellAside(
                    id=RIGHT_ASIDE_ID,
                    children=[],
                    zIndex=90,
                    style={'display': 'none'},
                    withBorder=True, visibleFrom='md'),

                dmc.AppShellFooter(id=FOOTER_ID, zIndex=100, children=[]),
            ],
            style={'padding-inline': '0px', 'background-color': '#f2f2f2'},
            header={'height': header_height},
            footer={'height': footer_height},
            navbar={'width': navbar_width,
                    'breakpoint': 'xl',
                    'collapsed': {'desktop': False, 'mobile': True},
                    },
            aside={'width': aside_width,
                   'breakpoint': 'xl',
                   'collapsed': {'desktop': False, 'mobile': True},
                   },
        )
    )
