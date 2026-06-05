import dash_mantine_components as dmc
from dash_iconify import DashIconify

from . import theme_config


def navbar_page_icon(icon: str, title: str, href: str, active: bool = False) -> dmc.Anchor:
    """
    Renders a navbar icon for a module page.
    """
    return dmc.Anchor([
        dmc.Tooltip(
            dmc.ActionIcon(
                DashIconify(icon=icon,
                            color=theme_config.PRIMARY_COLOR if active else 'gray',
                            width=32),
                variant='transparent',
                size='xl',
            ),
            label=dmc.Text(title, c='white' if active else '#656565'),
            position='right',
            color=theme_config.PRIMARY_COLOR if active else 'lightgray',
            transitionProps={
                'transition': 'scale-x',
                'duration': 200,
                'timingFunction': 'ease'
            },
        )
    ], href=href)
