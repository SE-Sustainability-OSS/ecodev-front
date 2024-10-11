"""
Module implementing a shadow-box component.
"""
import dash_mantine_components as dmc
from dash import html

def shadow_box(children: list[html.Div], 
               shadow_color: str, 
               radius: str = 'md',
               shadow_thickness: int = 8,
               style: dict = {}
               ) -> html.Div:
    """
    Renders a colored shadow around a dmc.Paper component.
    """
    return html.Div([
        dmc.Paper(children=children,
                  radius=radius,
                  style={'boxShadow': f"""{shadow_thickness}px 
                                          {shadow_thickness}px 
                                          2px 0px {shadow_color}""",
                         'padding': '30px'},
       ),
    ], style={'margin':'5px'} | style)
