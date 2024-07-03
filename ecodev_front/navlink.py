"""
File containg a navigation link component
"""
import dash_mantine_components as dmc
from dash_iconify import DashIconify


def navlink(label: str,
            href: str,
            icon: str | None = None) -> dmc.NavLink:
    """
    A simple navigation link component.
    """
    return dmc.NavLink(label=label,
                       leftSection=DashIconify(icon=icon),
                       href=href)
