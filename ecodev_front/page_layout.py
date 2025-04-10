"""
Module implementing a standardised page layout
"""
import dash_mantine_components as dmc

from ecodev_front.constants import INDEX
from ecodev_front.constants import TYPE
from ecodev_front.ids import PROJECT_HEADER_ID
from ecodev_front.page_header import page_title_header


def page_layout(page_id: str,
                title: str,
                icon: str,
                description: str,
                color: str = '#0066a1',
                icon_color: str = '#97BDD3',
                ) -> dmc.Stack:
    """
    Returns a standard page layout, with title header, project header placeholder
    and page content placeholder.
    """
    return dmc.Stack([
        dmc.Group([
            page_title_header(title, icon, description, color, icon_color),
            dmc.Group([
                dmc.Divider(orientation='vertical', size=2, mr=10),
                dmc.Stack(id={TYPE: PROJECT_HEADER_ID, INDEX: page_id},
                          gap=0, style={'minWidth': '150px'})
            ], w='35%', justify='flex-end')
        ], justify='space-between', align='center', w='100%'),
        dmc.Divider(w='100%'),
        dmc.Box(id=page_id, w='100%', h='100%', p=10)
    ], w='95%', m='auto', mt=10, style={'minHeight': '100vh'})
