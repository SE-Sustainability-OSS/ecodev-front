"""
Component which to display a dmc.Modal on the side of the screen
"""
from typing import Any

import dash_mantine_components as dmc


def modal(id: str,
          children: Any,
          size: int | str = '80%',
          with_close_button: bool = False,
          padding: int = 10
          ) -> dmc.Modal:
    """
    Returns a dmc.Modal which can be used to display content on the screen temporarily
    """
    return dmc.Modal(id=id, children=children, size=size, withCloseButton=with_close_button,
                     padding=padding)
