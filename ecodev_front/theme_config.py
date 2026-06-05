"""
Module-level theme configuration for ecodev_front.
Override defaults by calling configure_front_theme() early in your app (before layout construction).
"""
from typing import Any

PRIMARY_COLOR: str = '#008029'
ICON_COLOR: str = '#008029'
BACKGROUND_COLOR: str = '#f2f2f2'
DMC_THEME: dict[str, Any] | None = None


def configure_front_theme(
    primary_color: str | None = None,
    icon_color: str | None = None,
    background_color: str | None = None,
    dmc_theme: dict[str, Any] | None = None,
) -> None:
    """
    Override ecodev_front default theme values. Call once at app startup, before layout construction.
    Only provided (non-None) values are updated.
    """
    global PRIMARY_COLOR, ICON_COLOR, BACKGROUND_COLOR, DMC_THEME
    if primary_color is not None:
        PRIMARY_COLOR = primary_color
    if icon_color is not None:
        ICON_COLOR = icon_color
    if background_color is not None:
        BACKGROUND_COLOR = background_color
    if dmc_theme is not None:
        DMC_THEME = dmc_theme
