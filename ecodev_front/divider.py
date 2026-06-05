"""
File containing a page divider
"""
import dash_mantine_components as dmc

from ecodev_front.constants import MAIN_COLOR
from ecodev_front.constants import VERY_LIGHT_GRAY


def divider(orientation: str = 'horizontal',
            label: str | dmc.Anchor | None = None,
            position: str = 'center',
            margin: int = 10,
            w: str | int = '',
            color: str = MAIN_COLOR
            ) -> dmc.Divider:
    """
    Renders a divider
    """
    return dmc.Divider(orientation=orientation,
                       label=label, labelPosition=position,
                       m=margin, w=w, color=color)


def header_divider() -> dmc.Divider:
    """
    Generates the vertical navbar dividers between app header sections
    """
    return dmc.Divider(orientation='vertical',
                       style={'color': VERY_LIGHT_GRAY,
                              'marginTop': '10px',
                              'marginBottom': '10px'})
