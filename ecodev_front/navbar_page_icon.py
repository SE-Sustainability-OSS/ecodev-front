import dash_mantine_components as dmc
from dash_iconify import DashIconify

from ecodev_front import theme_config


def navbar_page_icon(icon: str,
                     title: str,
                     href: str,
                     active: bool = False,
                     color: str | None = None,
                     ) -> dmc.Anchor:
    """
    Renders a navbar icon for a module page.
    """
    resolved_color = color or theme_config.PRIMARY_COLOR
    return dmc.Anchor([
        dmc.Tooltip(
            dmc.ActionIcon(
                DashIconify(icon=icon,
                            color=resolved_color if active else 'gray',
                            width=32),
                variant='transparent',
                size='xl',
            ),
            label=dmc.Text(title, c='white' if active else theme_config.GRAY_COLOR),
            position='right',
            color=resolved_color if active else 'lightgray',
            transitionProps={
                'transition': 'scale-x',
                'duration': 200,
                'timingFunction': 'ease'
            },
        )
    ], href=href)
