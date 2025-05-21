"""
Module implementing a button component with a colored shadow.
"""
import dash_mantine_components as dmc
from dash import html
from dash_iconify import DashIconify

from ecodev_front.constants import INDEX
from ecodev_front.constants import TYPE
from ecodev_front.ids import MODULE_BUTTON


def shadow_button(id: str | dict[str, str],
                  children: list[html.Div],
                  shadow_color: str,
                  radius: str = 'md',
                  shadow_thickness: int = 8,
                  disabled: bool = False,
                  style: dict = {}
                  ) -> dmc.Button:
    """
    Renders a button component with a colored shadow
    """
    return html.Div([
        dmc.Paper(radius=radius,
                  style={'boxShadow': f"""{shadow_thickness}px
                                          {shadow_thickness}px
                                          2px 0px {shadow_color}"""},
                  children=[
                      dmc.Button(id=id,
                                 children=children,
                                 radius=radius,
                                 disabled=disabled,
                                 variant='subtle',
                                 style={'height': '100%',
                                        'width': '100%',
                                        'backgroundColor': 'white',
                                        'padding-top': '25px',
                                        'padding-bottom': '25px'}
                                 )
                  ])
    ], style={'margin': '10px'} | style
    )


def module_main_button(id: str,
                       icon: str,
                       label_top: str,
                       label_bottom: str,
                       color: str,
                       disabled: bool = False,
                       w: str | int = 230,
                       style: dict = {}) -> html.Div:
    """
    Renders a shadow_button with text above and below an icon
    """
    color = color if not disabled else '#dcdcdc'
    return shadow_button(
        id={TYPE: MODULE_BUTTON, INDEX: id},
        disabled=disabled,
        children=dmc.Stack([
            dmc.Text(label_top, fz='18', c=color),
            DashIconify(icon=icon, width=45, color=color),
            dmc.Text(label_bottom, fz='22', fw=700, c=color)
        ], align='center', gap='5px', style={'min-width': '100px'}),
        shadow_color=color,
        style={'min-width': 200, 'width': w, 'max-width': 280} | style
    )
