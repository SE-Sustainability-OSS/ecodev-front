from typing import Optional

import dash_mantine_components as dmc
from dash_iconify import DashIconify


def navlink(label: str,
            href: str,
            icon: Optional[str] = None) -> dmc.NavLink:
    """
    A simple navigation link component.
    """
    return dmc.NavLink(label=label,
                       leftSection=DashIconify(icon=icon),
                       href=href)
