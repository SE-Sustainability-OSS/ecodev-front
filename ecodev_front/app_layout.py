"""
Base app component, utilising dmc.AppShell.
"""
from typing import Any

import dash
import dash_mantine_components as dmc
from dash import dcc
from dash import html

from ecodev_front.button import ButtonAction
from ecodev_front.button import render_action_button
from ecodev_front.constants import ERROR
from ecodev_front.constants import INDEX
from ecodev_front.constants import NOTIFICATION_ID
from ecodev_front.constants import TYPE
from ecodev_front.ids import APPSHELL
from ecodev_front.ids import ASIDE
from ecodev_front.ids import ERROR_MODAL
from ecodev_front.ids import FOOTER_ID
from ecodev_front.ids import HEADER_ID
from ecodev_front.ids import INTERVAL
from ecodev_front.ids import MAIN_CONTENT_ID
from ecodev_front.ids import MODAL
from ecodev_front.ids import NAVBAR
from ecodev_front.ids import NOTIFICATION
from ecodev_front.ids import TEXT
from ecodev_front.ids import TOKEN
from ecodev_front.ids import URL
from ecodev_front.modal import modal


def get_error_monitor_component():
    """
    Get a hidden interval component to monitor errors.
    This should be added to the main layout.
    """
    return dcc.Interval(
        id={TYPE: INTERVAL, INDEX: ERROR},
        interval=2000,  # Check every 2 seconds
        n_intervals=0,
        disabled=False
    )


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
            dmc.NotificationContainer(id=NOTIFICATION),
            get_error_monitor_component(),
            modal(
                id={TYPE: MODAL, INDEX: ERROR},
                children=[
                    dmc.Stack([
                        dmc.Text(
                            id={TYPE: TEXT, INDEX: ERROR},
                            size='sm',
                            style={'whiteSpace': 'pre-wrap', 'fontFamily': 'monospace'}
                        ),
                        render_action_button(index=ERROR_MODAL, action=ButtonAction.CLOSE)
                    ])
                ],
                size='lg',
            ),
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
