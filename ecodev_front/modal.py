"""
Component which to display a dmc.Modal on the side of the screen
"""
from typing import Any

import dash_mantine_components as dmc


def modal(id: str | dict,
          children: Any = [],
          size: int | str = '80%',
          with_close_button: bool = False,
          padding: int = 10,
          close_on_escape: bool = True,
          close_on_click_outside: bool = True,
          title: Any = None,
          opened: bool = False,
          centered: bool = False,
          keep_mounted: bool = False,
          z_index: int | None = None
          ) -> dmc.Modal:
    """
    Returns a dmc.Modal which can be used to display content on the screen temporarily
    - title: optional header content (text or component)
    - keep_mounted: keeps the children in the DOM while closed, so callbacks can read them
    """
    optional_props = {'title': title, 'zIndex': z_index}
    return dmc.Modal(id=id, children=children, size=size, withCloseButton=with_close_button,
                     padding=padding, closeOnEscape=close_on_escape,
                     closeOnClickOutside=close_on_click_outside, opened=opened,
                     centered=centered, keepMounted=keep_mounted,
                     **{k: v for k, v in optional_props.items() if v is not None})
