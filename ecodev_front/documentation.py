import dash_mantine_components as dmc
from dash import html

from ecodev_front.constants import INDEX
from ecodev_front.constants import TYPE
from ecodev_front.ids import ACTION_ITEM
from ecodev_front.ids import DOCUMENTATION
from ecodev_front.nav_items import action_item
from ecodev_front.text import subtitle


def documentation_icon_link(icon_width: int = 30,
                            icon_color: str = '#8BC1E3') -> html.Div:
    """
    Renders the documentation action item to go to the documentation section
    """
    return action_item(id={TYPE: ACTION_ITEM, INDEX: DOCUMENTATION},
                       label=DOCUMENTATION,
                       icon='bxs:book',
                       href=f'/{DOCUMENTATION}',
                       icon_color=icon_color,
                       icon_width=icon_width)


def documentation_text(text: str = """If this is your first time using this tool, we
                    recommend you read through the documentation.""",
                       icon_width: int = 50) -> dmc.Group:
    """
    Renders the text accompanying the documentation button
    """

    return dmc.Group([
        subtitle(text, ta='left'),
        documentation_icon_link(icon_width)
    ], justify='space-around')
