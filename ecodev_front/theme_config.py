"""
Module-level theme configuration for ecodev_front.
Override defaults by calling configure_front_theme() early in your app (before layout construction).
"""
from typing import Any

PRIMARY_COLOR: str = '#0066a1'
SECONDARY_COLOR: str = '#5da6d1'
WHITE_COLOR: str = '#ffffff'
BLACK_COLOR: str = '#000000'
GRAY_COLOR: str = '#808080'
BACKGROUND_COLOR: str = '#f2f2f2'
DMC_THEME: dict[str, Any] | None = None


def configure_front_theme(
    primary_color: str | None = None,
    secondary_color: str | None = None,
    background_color: str | None = None,
    dmc_theme: dict[str, Any] | None = None,
) -> None:
    """
    Override ecodev_front default theme values. Call once at app startup, before layout construction.
    Only provided (non-None) values are updated.
    """
    global PRIMARY_COLOR, SECONDARY_COLOR, BACKGROUND_COLOR, DMC_THEME
    if primary_color is not None:
        PRIMARY_COLOR = primary_color
    if secondary_color is not None:
        SECONDARY_COLOR = secondary_color
    if background_color is not None:
        BACKGROUND_COLOR = background_color
    if dmc_theme is not None:
        DMC_THEME = dmc_theme
