"""
File containing a navigation link component
"""
import dash_mantine_components as dmc

from ecodev_front import dash_icon


def navlink(
    label: str,
    icon: str,
    href: str = '',
    id: str = '',
    children: list | None = None,
    target: str | None = None,
    active: str | bool | None = None,
    opened: bool = False,
    children_offset: int | None = None,
) -> dmc.NavLink:
    """
    Navigation link component, supports both leaf links and tree parent nodes.
    """
    return dmc.NavLink(
        label=label,
        leftSection=dash_icon(icon=icon),
        href=href or None,
        id=id,
        children=children,
        target=target,
        active=active,
        opened=opened,
        childrenOffset=children_offset,
    )
