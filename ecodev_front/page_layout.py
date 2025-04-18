"""
Module implementing standardised page layouts
"""
import dash_mantine_components as dmc

from ecodev_front.aside_buttons import aside_buttons
from ecodev_front.constants import INDEX
from ecodev_front.constants import TYPE
from ecodev_front.ids import PROJECT_HEADER_ID
from ecodev_front.page_header import page_title_header
from ecodev_front.page import Page


def basic_layout(page: Page) -> dmc.Stack:
    """
    Renders a basic layout (no header, simply a div with page.id) and aside buttons
    """
    return dmc.Stack([
        aside_buttons(),
        dmc.ScrollArea(id=page.id, w='100%', h='81vh', pr=25, mb=100, offsetScrollbars='50px')
    ], w='97%', m='auto', mt=20, style={'height': '95vh'}, mb=20)


def header_layout(page: Page,
                  color: str = '#0066a1',
                  icon_color: str = '#97BDD3',
                  ) -> dmc.Stack:
    """
    Returns a standard page layout, with title header, project header placeholder
    and page content placeholder. And aside buttons.
    """
    return dmc.Stack([
        aside_buttons(),
        dmc.Group([
            page_title_header(page.title, page.icon, page.description, color, icon_color),
            dmc.Group([
                dmc.Divider(orientation='vertical', size=2, mr=10),
                dmc.Stack(id={TYPE: PROJECT_HEADER_ID, INDEX: page.id},
                          gap=0, style={'minWidth': '150px'})
            ], w='35%', justify='flex-end')
        ], justify='space-between', align='center', w='100%'),
        dmc.Divider(w='100%'),
        dmc.ScrollArea(id=page.id, w='100%', h='81vh', pr=25, mb=100)
    ], w='97%', m='auto', mt=0, style={'height': '95vh'}, mb=20)

