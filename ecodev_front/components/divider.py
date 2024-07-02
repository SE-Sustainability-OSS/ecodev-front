from typing import Union

import dash_mantine_components as dmc


def divider(orientation: str = 'horizontal',
            margin: int = 10,
            w: Union[str, int] = '') -> dmc.Divider:
    """
    Renders a divider
    """
    return dmc.Divider(orientation=orientation, m=margin, w=w)
