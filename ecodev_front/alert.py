"""
Module implementing a dmc.Alert component
"""
from typing import Any

import dash_mantine_components as dmc
from dash.development.base_component import Component


def alert(title: str | None = None,
          message: str | Component | list[Component] | None = None,
          color: str = 'primary',
          width: int | str = '100%',
          style: dict[str, str] | None = None,
          **kwargs: Any) -> dmc.Alert:
    """
    Returns an alert (text specifically formatted with a title, a message and a background color)
    - title: text that will be displayed on the top of the alert
    - message: text, dmc.Text, list of dmc.Text or any component displayed in the body
    - color: color of the alert background (e.g., 'green', 'red', 'blue')
    - kwargs: any other dmc.Alert prop (e.g., variant, icon, p), passed through as is
    """
    props = {'title': title, 'children': message}
    return dmc.Alert(
        color=color,
        w=width,
        style=style or {},
        **{k: v for k, v in props.items() if v is not None},
        **kwargs
    )
