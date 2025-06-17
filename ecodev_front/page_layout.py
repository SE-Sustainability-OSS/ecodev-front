"""
Module implementing standardised page layouts
"""
import dash_mantine_components as dmc

from ecodev_front.aside_buttons import aside_buttons
from ecodev_front.constants import INDEX
from ecodev_front.constants import TYPE
from ecodev_front.ids import PROJECT_HEADER_ID
from ecodev_front.page import Page
from ecodev_front.page_header import page_title_header


def basic_layout(page: Page,
                 enable_scroll: bool = True,
                 aside_width: int | str | None = None) -> dmc.Stack:
    """
    Renders a basic layout (no header, simply a div/scroll-area with page.id) and aside buttons.
    NOTE: If disabling the scroll area, ensure that your page content fits !
    """
    return dmc.Stack([
        (dmc.ScrollArea(dmc.Stack(id=page.id, mb=100, w='100%'),
                        w='100%', h='85vh', pr=25, mb=0, offsetScrollbars='50px')
         if enable_scroll else
         dmc.Stack(id=page.id, w='98%', h='90vh', m='auto', mt=0, pt=0)),
        aside_buttons(aside_width) if aside_width else aside_buttons(),
    ], w='97%', m='auto', mt=5, style={'height': '95vh'}, mb=0)


def header_layout(page: Page,
                  color: str = '#0066a1',
                  with_icon: bool = True,
                  icon_color: str = '#97BDD3',
                  enable_scroll: bool = True,
                  aside_width: int | str | None = None
                  ) -> dmc.Stack:
    """
    Returns a page with title header, project header placeholder, aside buttons,
    and page content placeholder.
    """
    return dmc.Stack([
        dmc.Group([
            page_title_header(page.title, with_icon, page.icon,
                              page.description, color, icon_color),
            dmc.Group([
                dmc.Divider(orientation='vertical', size=2, mr=10),
                dmc.Stack(id={TYPE: PROJECT_HEADER_ID, INDEX: page.id},
                          gap=0, style={'minWidth': '150px'})
            ], w='35%', justify='flex-end')
        ], justify='space-between', align='center', w='100%'),
        dmc.Divider(w='100%'),
        (dmc.ScrollArea(dmc.Stack(id=page.id, mb=100, w='100%'),
                        w='100%', h='81vh', pr=25, mb=0, offsetScrollbars='50px')
         if enable_scroll else
         dmc.Stack(id=page.id, w='98%', h='81vh', m='auto', mt=0, pt=0)),
        aside_buttons(aside_width) if aside_width else aside_buttons(),
    ], w='97%', m='auto', mt=5, style={'height': '96vh'}, mb=0)
