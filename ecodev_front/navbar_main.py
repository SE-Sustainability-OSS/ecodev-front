"""
Module implementing an example of customisable navbar components.
"""
from typing import Dict

import dash_mantine_components as dmc
from dash import html

from ecodev_front.nav_items import navbar_action_item
from ecodev_front.nav_items import navbar_menu
from ecodev_front.navbar_header import navbar_header
from ecodev_front.navbar_login import navbar_login

NAVBAR_DIVIDER = dmc.Divider(orientation='vertical',
                             style={'margin-top': '10px', 'margin-bottom': '10px'})


def navbar(is_user: bool = False,
           is_admin: bool = False,
           navbar_menus: Dict[str, Dict[str, str]] = None) -> html.Div:
    """
    Function which determines the display of the various navbar buttons.
    I.e. Only show navbar to users, and only show certain additional buttons to admin users.
    """
    component = dmc.Grid(children=[navbar_header()])
    if is_user:
        component.children.append(navbar_app_pages(navbar_menus))
        component.children.append(user_admin_settings(is_admin))
        return html.Div([component])

    component.children.append(navbar_login())
    return html.Div([component])


def navbar_app_pages(navbar_menus: Dict[str, Dict[str, str]]) -> dmc.GridCol:
    """
    Example of how to create / assemble the navbar for the app specific pages.
    """

    navbar_menus = [
        navbar_action_item(
            id=label,
            label=label,
            icon=navbar_menus.get(label).get('icon'),
            href=navbar_menus.get(label).get('href'),
        )
        for label in navbar_menus
    ]
    [NAVBAR_DIVIDER] * len(navbar_menus)
    # inputs_example_menu = navbar_menu(
    #     label='INPUTS EXAMPLES',
    #     icon='clarity:form-line',
    #     menu_items=[
    #         navbar_menu_item(
    #             label='Forms', href='/inputs/forms', icon='solar:text-field-linear'
    #         ),
    #         navbar_menu_item(
    #             label='Search bar', href='/inputs/search-bar', icon='basil:search-solid'
    #         ),
    #         navbar_menu_item(
    #             label='Data table', href='/inputs/data-table', icon='uiw:table'
    #         ),
    #         navbar_menu_item(
    #             label='Upload box',
    #             href='/inputs/file-upload',
    #             icon='material-symbols:upload',
    #         ),
    #     ],
    # )
    #
    # outputs_example_menu = navbar_menu(
    #     label='OUTPUTS EXAMPLES',
    #     icon='mdi:graph-box-outline',
    #     menu_items=[
    #         navbar_menu_item(label='Reports', href='/outputs/reports', icon='gg:notes'),
    #         navbar_menu_item(
    #             label='Graphs/Dashboards',
    #             href='/outputs/dashboards',
    #             icon='ic:round-dashboard',
    #         ),
    #         navbar_menu_item(
    #             label='Tabular', href='/outputs/data-table', icon='ph:table-bold'
    #         ),
    #         navbar_menu_item(label='Map', href='/outputs/map', icon='tabler:map-pin-2'),
    #     ],
    # )

    return dmc.GridCol(
        [
            dmc.Group(
                navbar_menus,
                justify='space-around',
            ),
        ],
        span='auto',
    )


def user_admin_settings(is_admin: bool,
                        documentation_href: str = 'https://ecosia.com'
                        ) -> dmc.GridCol:
    """
    Example of how to create / assemble the navbar for the user/admin specific pages.
    """
    logout_btn = navbar_action_item(
        id='logout-button', label='LOGOUT', icon='ic:baseline-logout', href='/'
    )

    doc_btn = navbar_action_item(
        id='documentation',
        label='DOCUMENTATION',
        icon='bxs:book',
        href=documentation_href,
        in_new_tab=True,
    )

    admin_menu = navbar_menu(
        label='ADMIN',
        icon='eos-icons:admin-outlined',
        # menu_items=[
        #     navbar_menu_item(
        #         label='Add user', href='/create-user', icon='mingcute:user-add-fill'
        #     ),
        #     navbar_menu_item(
        #         label='Edit database', href='/sql-admin', icon='octicon:database-16'
        #     ),
        # ],
    )

    return dmc.GridCol(
        [
            dmc.Group(
                [
                    admin_menu if is_admin else None,
                    NAVBAR_DIVIDER,
                    doc_btn,
                    NAVBAR_DIVIDER,
                    logout_btn,
                ],
                justify='flex-end',
                style={'margin-right': '20px'},
            ),
        ],
        span='auto',
    )
