"""
Module implementing a page header components
"""
import dash_mantine_components as dmc
from dash_iconify import DashIconify


def page_title_header(title: str,
                      icon: str,
                      description: str,
                      color: str = '#0066a1',
                      icon_color: str = '#97BDD3',
                      ) -> dmc.Stack:
    """
    Returns the header of the page.
    """
    return dmc.Group([
        dmc.Box(DashIconify(icon=icon,
                            width=36, height=36,
                            style={'color': '#f2f2f2', 'display': 'flex'}),
                style={'backgroundColor': icon_color,
                       'borderRadius': '8px', 'padding': '7px'}),
        dmc.Stack([
            dmc.Title(title, fz=18, c=color, fw=700, ta='left'),
            dmc.Text(description, fz=16, fs='italic', c='dimmed', truncate=True, ta='left')
        ], gap=0, w='90%')
    ], w='60%')


def page_project_header(name: str, description: str) -> dmc.Stack:
    """
    Returns a project header section.
    Name and description params only refer to how these items are presented in the front end.
    """
    return dmc.Stack([
        dmc.Title(name, fz=16, c='dimmed', fw=700, ta='left'),
        dmc.Text(description, fz=14, fs='italic', c='dimmed', truncate=True, ta='left')
    ], justify='flex-start', w='100%')
