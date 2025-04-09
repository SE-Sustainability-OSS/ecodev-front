"""
Module implementing a page header components
"""
import dash_mantine_components as dmc
from dash_iconify import DashIconify

from ecodev_front.constants import INDEX
from ecodev_front.constants import TYPE
from ecodev_front.ids import PROJECT_HEADER_ID


def page_header(page_id: str,
                title: str,
                icon: str,
                description: str,
                color: str = '#0066a1',
                icon_color: str = '#97BDD3',
                ) -> dmc.Stack:
    """
    Returns the header of the page.
    """
    return dmc.Stack([
        dmc.Group([
            dmc.Group([
                dmc.Box(DashIconify(icon=icon,
                                    width=36, height=36,
                                    style={'color': '#f2f2f2', 'display': 'flex'}),
                        style={'backgroundColor': icon_color,
                               'borderRadius': '8px', 'padding': '7px'}),
                dmc.Stack([
                    dmc.Title(title, fz=18, c=color, fw=700),
                    dmc.Text(description, fz=16, fs='italic', c='dimmed', truncate=True)
                ], gap=0)
            ], w='60%'),
            dmc.Group([
                dmc.Divider(orientation='vertical', size=2, mr=10),
                dmc.Stack(id={TYPE: PROJECT_HEADER_ID, INDEX: page_id},
                          gap=0, style={'minWidth': '150px'})
            ], w='35%', justify='flex-end')
        ], justify='space-between', align='center', w='100%'),
        dmc.Divider(w='100%'),
        dmc.Box(id=page_id, w='100%', h='100%', p=10)
    ], w='95%', m='auto', mt=10, style={'minHeight': '100vh'})


def page_project_header(name: str, description: str) -> dmc.Stack:
    """
    Returns a project header section.
    Name and description params only refer to how these items are presented in the front end.
    """
    return dmc.Stack([
        dmc.Title(name, fz=16, c='dimmed', fw=700, ta='left'),
        dmc.Text(description, fz=14, fs='italic', c='dimmed', truncate=True, ta='left')
    ], justify='flex-start', w='100%')
