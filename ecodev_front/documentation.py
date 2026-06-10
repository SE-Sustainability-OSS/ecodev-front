import dash_mantine_components as dmc
from dash import html
from dash_iconify import DashIconify

from ecodev_front import theme_config
from ecodev_front.constants import INDEX
from ecodev_front.constants import TYPE
from ecodev_front.ids import ACTION_ITEM
from ecodev_front.ids import DOCS_LINK_ID
from ecodev_front.ids import DOCUMENTATION
from ecodev_front.nav_items import action_item
from ecodev_front.text import subtitle


def documentation_icon_link(icon_width: int = 30,
                            icon_color: str | None = None) -> html.Div:
    """
    Renders the documentation action item to go to the documentation section
    """
    return action_item(id={TYPE: ACTION_ITEM, INDEX: DOCUMENTATION},
                       label=DOCUMENTATION,
                       icon='bxs:book',
                       href=f'/{DOCUMENTATION}',
                       icon_color=icon_color or theme_config.SECONDARY_COLOR,
                       icon_width=icon_width)


def html_docs_link(icon_color: str | None = None, icon_width: int = 30) -> dmc.Tooltip:
    """
    Docs link anchored at /docs/ — id is on the Anchor so a clientside_callback can update href.
    Used for Flask-served MkDocs sites protected by JWT session auth.
    """
    return dmc.Tooltip(
        label='DOCUMENTATION',
        style={'background-color': 'white', 'color': 'grey', 'font-size': '12px'},
        position='bottom',
        offset=10,
        children=[
            dmc.Anchor(
                id={TYPE: ACTION_ITEM, INDEX: DOCS_LINK_ID},
                href='/docs/',
                target='_blank',
                children=[
                    dmc.ActionIcon(
                        DashIconify(icon='bxs:book',
                                    color=icon_color or theme_config.SECONDARY_COLOR,
                                    width=icon_width),
                        size='xl',
                        variant='transparent',
                    )
                ],
            )
        ],
    )


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
