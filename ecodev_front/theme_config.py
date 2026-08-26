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
DARK_GRAY_COLOR: str = '#424242'
BACKGROUND_COLOR: str = '#f2f2f2'
DMC_THEME: dict[str, Any] | None = None

IMG_ICON_COLORS: dict[str, str] = {}
"""
Extra named colors (color-name suffix -> hex value) available for 'img:'-prefixed icon variant
matching (see ecodev_front.icon.dash_icon), on top of the 7 built-in names derived from the
theme values above. Populated via configure_front_theme(img_icon_colors=...) for apps whose
'<base>-<color-name>.png' icon variants use a richer/branded palette than those 7 names.
"""


def configure_front_theme(
    primary_color: str | None = None,
    secondary_color: str | None = None,
    background_color: str | None = None,
    dmc_theme: dict[str, Any] | None = None,
    img_icon_colors: dict[str, str] | None = None,
) -> None:
    """
    Override ecodev_front default theme values. Call once at app startup, before layout construction.
    Only provided (non-None) values are updated. img_icon_colors is merged into (rather than
    replacing) the existing registered colors, so repeated calls accumulate rather than clobber.
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
    if img_icon_colors is not None:
        IMG_ICON_COLORS.update(img_icon_colors)
