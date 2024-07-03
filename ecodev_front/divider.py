"""
File containing a page divider
"""
import dash_mantine_components as dmc


def divider(orientation: str = 'horizontal',
            margin: int = 10,
            w: str | int = '') -> dmc.Divider:
    """
    Renders a divider
    """
    return dmc.Divider(orientation=orientation, m=margin, w=w)
