"""
Base app component, utilising dmc.AppShell.
"""
from typing import Any

import dash
import dash_mantine_components as dmc
from dash import dcc
from dash import html

from ecodev_front.constants import NOTIFICATION_ID
from ecodev_front.ids import APPSHELL
from ecodev_front.ids import ASIDE
from ecodev_front.ids import FOOTER_ID
from ecodev_front.ids import HEADER_ID
from ecodev_front.ids import MAIN_CONTENT_ID
from ecodev_front.ids import NAVBAR
from ecodev_front.ids import TOKEN
from ecodev_front.ids import URL


def dash_base_layout(stores: list[dcc.Store] = [],
                     main_color: str = '#0066A1',
                     theme: dict[str, dict[str, Any] | list[str]] | None = None,
                     header_height: int = 55,
                     footer_height: int = 40,
                     main_content_style: dict[str, str] | None = None
                     ) -> dmc.MantineProvider:
    """
    Returns a base layout for any Dash application
    """
    return dmc.MantineProvider(
        forceColorScheme='light',
        theme=theme,
        children=dmc.AppShell([
            dcc.Location(id=URL, refresh='callback-nav'),
            dcc.Store(id=TOKEN, data={TOKEN: None}, storage_type='local'),
            *stores,

            html.Div(id=NOTIFICATION_ID),
            dmc.NotificationProvider(position='top-center'),

            dmc.AppShellHeader(id=HEADER_ID,
                               style={'background-color': main_color},
                               zIndex=100,
                               children=[],
                               ),

            dmc.AppShellMain(
                id=MAIN_CONTENT_ID,
                children=html.Div(style={'width': '100%'},
                                  children=dash.page_container),
                style=main_content_style or {'width': '100%',
                                             'justifyContent': 'center',
                                             'display': 'flex',
                                             'overflow': 'hidden',
                                             },
            ),

            dmc.AppShellFooter(id=FOOTER_ID, zIndex=100, children=[],
                               style={'paddingBottom': '50px',
                                      'backgroundColor': main_color,
                                      'color': 'white',
                                      'textAlign': 'center',
                                      'alignContent': 'center',
                                      'justifyContent': 'center'}
                               ),

            dmc.AppShellNavbar(
                id=NAVBAR,
                children=[],
                zIndex=90,
                withBorder=True,
                visibleFrom='md',
                className='my-navbar'
            ),

            dmc.AppShellAside(
                id=ASIDE,
                children=[],
                zIndex=90,
                withBorder=True,
                visibleFrom='md'
            )],

            id=APPSHELL,
            style={'padding': '0',
                   'background-color': '#f2f2f2',
                   'overflow': 'hidden',
                   'height': '96vh'},
            header={'height': header_height},
            footer={'height': footer_height},
            navbar={
                'breakpoint': 'xl',
                'collapsed': {'desktop': False, 'mobile': True},
        },
            aside={
                'breakpoint': 'xl',
                'collapsed': {'desktop': False, 'mobile': True},
        },
        )
    )
