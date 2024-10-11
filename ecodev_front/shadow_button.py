"""
Module implementing a button component with a colored shadow.
"""
import dash_mantine_components as dmc
from dash import html

def shadow_button(id: str,
                  children: list[html.Div],
                  shadow_color: str,
                  radius: str = 'md',
                  shadow_thickness: int = 8,
                  style: dict = {}
                  )  -> dmc.Button:
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
                                       variant='subtle',
                                       style={'height': '100%', 
                                              'width': '100%', 
                                              'backgroundColor': 'white',
                                              'padding-top':'25px',
                                              'padding-bottom':'25px'}
                            )
                     ])
              ], style={'margin':'10px'} | style
       )