"""
Module implementing a page divider
"""
import dash_mantine_components as dmc

from . import theme_config


def divider(orientation: str = 'horizontal',
            label: str | dmc.Anchor | None = None,
            position: str = 'center',
            margin: int = 10,
            w: str | int = '',
            color: str | None = None
            ) -> dmc.Divider:
    """
    Renders a divider
    """
    return dmc.Divider(orientation=orientation,
                       label=label, labelPosition=position,
                       m=margin, w=w, color=color or theme_config.PRIMARY_COLOR)


def header_divider() -> dmc.Divider:
    """
    Generates the vertical navbar dividers between app header sections
    """
    return dmc.Divider(orientation='vertical',
                       style={'color': '#f2f2f2',
                              'marginTop': '10px',
                              'marginBottom': '10px'})
