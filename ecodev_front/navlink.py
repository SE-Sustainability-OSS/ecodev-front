"""
File containing a navigation link component
"""
import dash_mantine_components as dmc

from ecodev_front import dash_icon


def navlink(label: str,
            href: str,
            icon: str,
            id: str = ''
            ) -> dmc.NavLink:
    """
    A simple navigation link component.
    """
    return dmc.NavLink(label=label, leftSection=dash_icon(icon=icon), href=href, id=id)
