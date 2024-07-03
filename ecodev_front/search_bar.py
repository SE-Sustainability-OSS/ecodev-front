"""
Component to search something in databases.

Note: Typically only used as the main search bar on a page.
"""
from typing import Dict
from typing import Union

import dash_mantine_components as dmc
from dash import html
from dash_iconify import DashIconify


def search_bar(id: str,
               label: str,
               helper: str,
               helper_text_color: str = 'gray',
               style: Union[Dict[str, str], None] = None,
               icon: str = 'quill:search',
               debounce: int = 750) -> html.Div:
    """
    Component to create a centered big / main search bar.

    Note: Default style has a width of 50vh.
    """
    style = style or {'width': '50vh'}
    return html.Div([
        dmc.Stack([
            dmc.TextInput(id=id,
                          placeholder=label,
                          leftSection=DashIconify(icon=icon, width=20),
                          radius='xl', size='lg',
                          debounce=debounce,
                          style=style),
            dmc.Text(helper, size='sm', fs='italic', c=helper_text_color)
        ])
    ], style={'display': 'flex',
              'justifyContent': 'center',
              'alignItems': 'center',
              'textAlign': 'center'})
