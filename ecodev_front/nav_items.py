"""
Module containing navbar item component generators.
"""
import dash_mantine_components as dmc
from dash import html
from dash_iconify import DashIconify


def navbar_action_item(id: str,
                       label: str,
                       icon: str,
                       href: str,
                       icon_color: str = 'white',
                       in_new_tab: bool = False) -> html.Div:
    """
    A navbar action item (i.e. icon button without a menu).
    These can be opened in a new tab & can have callbacks associated with the id provided.
    """
    target = '_blank' if in_new_tab else '_self'
    return html.Div(children=[
        dmc.Tooltip(
            label=label.upper(),
            style={'background-color': 'white',
                   'color': 'grey',
                   'font-size': '12px'},
            position='bottom',
            offset=9,
            children=[
                dmc.Anchor(href=href,
                           target=target,
                           children=[
                               dmc.ActionIcon(
                                   DashIconify(icon=icon,
                                               color=icon_color,
                                               width=35),
                                   id=id,
                                   size='xl',
                                   variant='transparent',
                                   n_clicks=0,
                               ),
                           ])
            ])
    ], style={'display': 'flex',
              'justifyContent': 'center',
              'alignItems': 'center',
              'textAlign': 'center'})


def navbar_menu(label: str,
                icon: str,
                # menu_items: List[dmc.MenuItem],
                icon_color: str = 'white') -> html.Div:
    """
    Component to create a navbar menu.
    The menu items must be created beforehand & passed to this component.
    """
    return html.Div(children=[
        dmc.Menu([
            dmc.MenuTarget(dmc.ActionIcon(
                DashIconify(icon=icon,
                            color=icon_color, width=35),
                size='xl',
                variant='transparent',
                id='action-icon',
                n_clicks=0,
            )),
            # dmc.MenuDropdown([dmc.MenuLabel(label.upper()),
            #                   html.Div([item for item in menu_items])
            #                   ])
        ], offset=9, trigger='hover')
    ], style={'display': 'flex',
              'justifyContent': 'center',
              'alignItems': 'center',
              'textAlign': 'center'})


def navbar_menu_item(label: str,
                     href: str,
                     icon: str,
                     icon_color: str = '#0066A1') -> dmc.MenuItem:
    """
    Component to create a navbar menu item.
    """
    return dmc.MenuItem(
        label,
        href=href,
        target='_self',
        leftSection=DashIconify(icon=icon, color=icon_color, width=20),
    )


def navbar_divider() -> dmc.Divider:
    """
    Generates the vertical navbar dividers between sections
    """
    return dmc.Divider(orientation='vertical',
                       style={'color': '#f2f2f2',
                              'marginTop': '10px',
                              'marginBottom': '10px'})
