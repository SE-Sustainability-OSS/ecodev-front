"""
Module implementing a dmc.Alert component
"""
from typing import List

import dash_mantine_components as dmc


def alert(title: str,
          message: str | dmc.Text | List[dmc.Text],
          color: str,
          width: int | str = '100%',
          style: dict[str, str] | None = None) -> dmc.Alert:
    """
    Returns an alert (text specifically formatted with a title, a message and a background color)
    - title: text that will be displayed on the top of the alert
    - message: text that will be displayed in the body of the alert
    - color: color of the alert background (e.g., 'green', 'red', 'blue')
    """
    return dmc.Alert(
        title=title,
        children=message,
        color=color,
        w=width,
        style=style or {}
    )
