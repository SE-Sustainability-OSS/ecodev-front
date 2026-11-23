"""
Module implementing a dmc.Alert component
"""
from typing import Any

import dash_mantine_components as dmc
from dash.development.base_component import Component


def alert(title: str | None = None,
          message: str | Component | list[Component] | None = None,
          color: str = 'blue',
          width: int | str = '100%',
          style: dict[str, str] | None = None,
          variant: str | None = None,
          icon: Any = None) -> dmc.Alert:
    """
    Returns an alert (text specifically formatted with a title, a message and a background color)
    - title: text that will be displayed on the top of the alert
    - message: text, dmc.Text, list of dmc.Text or any component displayed in the body
    - color: color of the alert background (e.g., 'green', 'red', 'blue')
    - variant: Mantine alert variant (e.g., 'light', 'outline'), Mantine default when omitted
    - icon: component displayed on the left of the alert (e.g., a DashIconify)
    """
    optional_props = {'title': title, 'children': message, 'variant': variant, 'icon': icon}
    return dmc.Alert(
        color=color,
        w=width,
        style=style or {},
        **{k: v for k, v in optional_props.items() if v is not None}
    )
