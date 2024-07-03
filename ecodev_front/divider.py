"""
File containing a page divider
"""
import dash_mantine_components as dmc


def divider(orientation: str = 'horizontal',
            label: str | None = None,
            position: str = 'center',
            margin: int = 10,
            w: str | int = '') -> dmc.Divider:
    """
    Renders a divider
    """
    return dmc.Divider(orientation=orientation,
                       label=label, labelPosition=position,
                       m=margin, w=w)


def header_divider() -> dmc.Divider:
    """
    Generates the vertical navbar dividers between app header sections
    """
    return dmc.Divider(orientation='vertical',
                       style={'color': '#f2f2f2',
                              'marginTop': '10px',
                              'marginBottom': '10px'})
