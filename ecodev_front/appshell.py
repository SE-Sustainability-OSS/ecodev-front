from typing import Dict

import dash
import dash_mantine_components as dmc
from dash import dcc

from ecodev_front.footer import app_footer
from ecodev_front.ids import NAVBAR
from ecodev_front.ids import TOKEN
from ecodev_front.ids import URL


def dash_base_layout(stores: Dict[str, str]) -> dmc.MantineProvider:
    """
    Returns a base layout for any Dash application
    """
    stores = [dcc.Store(id=store_id, storage_type=storage_type) for store_id, storage_type in
              stores.items()]

    return dmc.MantineProvider(
        forceColorScheme='light',
        children=dmc.AppShell(
            [
                dcc.Location(id=URL, refresh=True),
                dcc.Store(id=TOKEN, data={TOKEN: None}, storage_type='local'),
                stores[0],
                dmc.AppShellHeader(id=NAVBAR, children=[], style={'background-color': '#0066A1'}),
                dmc.AppShellMain(dash.page_container, style={'margin-top': '2%'}),
                dmc.AppShellFooter(app_footer()),
            ],
            style={'padding-inline': '0px', 'background-color': '#f2f2f2'},
            header={'height': 55},
            footer={'height': 40},
        )
    )
