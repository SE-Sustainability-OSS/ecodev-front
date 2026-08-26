"""
Module implementing icon rendering, either as a dash-iconify icon or as an image.

An icon string is rendered as an image (rather than through dash-iconify) when it is
'img:'-prefixed (e.g. 'img:/assets/img/icons/pages/encore'), with dash_icon then picking
whichever '<base>-<color-name>.png' variant most closely matches the requested render color,
falling back to a plain '<base>.png' when no color variant exists on disk. Any icon string
that isn't 'img:'-prefixed is rendered through dash-iconify, unchanged from before.
"""
from pathlib import Path

import dash
import dash_mantine_components as dmc
from dash_iconify import DashIconify

from ecodev_front import theme_config

IMG_ICON_PREFIX = 'img:'


def is_img_icon(icon: str) -> bool:
    """
    Returns whether an icon string is an image (IMG_ICON_PREFIX-prefixed) rather than a
    dash-iconify icon name.
    """
    return icon.startswith(IMG_ICON_PREFIX)


def dash_icon(icon: str,
              width: int | None = None,
              height: int | None = None,
              color: str = 'default-color') -> DashIconify | dmc.Image:
    """
    Renders an icon string: a dash-iconify icon, or (for an 'img:'-prefixed icon) an image using
    whichever color variant on disk most closely matches the requested color.
    """
    if not is_img_icon(icon):
        return DashIconify(icon=icon, width=width, height=height, color=color)

    resolved_size = width or height
    if not (variants := _available_img_variants(icon)):
        return dmc.Image(src=f'{icon.removeprefix(IMG_ICON_PREFIX)}.png',
                         w=resolved_size, h=resolved_size)

    return dmc.Image(src=_closest_img_color_variant(variants, color),
                     w=resolved_size, h=resolved_size)


def _available_img_variants(icon: str) -> dict[str, str]:
    """
    Returns the {hex color: url path} mapping of every '<base>-<color-name>.png' variant that
    actually exists on disk (under the running app's assets folder), for an 'img:<base>' icon
    string. Color names checked are the current theme's named colors (see theme_config), so that
    apps overriding theme_config via configure_front_theme() get matching variant lookups.
    """
    base = icon.removeprefix(IMG_ICON_PREFIX)
    relative_base = base.removeprefix('/assets/')
    assets_folder = Path(dash.get_app().config.assets_folder)
    return {color_hex: f'{base}-{color_name}.png'
            for color_name, color_hex in _theme_color_palette().items()
            if (assets_folder / f'{relative_base}-{color_name}.png').exists()}


def _theme_color_palette() -> dict[str, str]:
    """
    Returns the named colors available for 'img:' icon variant matching, as {color-name suffix:
    hex value}: the 7 built-in names read live from theme_config (so overrides via
    configure_front_theme() are reflected), plus any extra names an app registered via
    configure_front_theme(img_icon_colors=...) (which take priority on name clashes).
    """
    return {
        'white': theme_config.WHITE_COLOR,
        'black': theme_config.BLACK_COLOR,
        'primary': theme_config.PRIMARY_COLOR,
        'secondary': theme_config.SECONDARY_COLOR,
        'gray': theme_config.GRAY_COLOR,
        'darkgray': theme_config.DARK_GRAY_COLOR,
        'background': theme_config.BACKGROUND_COLOR,
    } | theme_config.IMG_ICON_COLORS


def _closest_img_color_variant(variants: dict[str, str], color: str) -> str:
    """
    Returns the image path in variants (a hex color -> image path mapping) whose hex color is
    closest (RGB euclidean distance) to the requested color, or an arbitrary variant when color
    isn't a resolvable hex string (e.g. the 'default-color' sentinel).
    """
    if not (target_rgb := _hex_to_rgb(color)):
        return next(iter(variants.values()))
    return min(variants.items(),
               key=lambda variant: sum((a - b) ** 2
                                       for a, b in zip(_hex_to_rgb(variant[0]), target_rgb)))[1]


def _hex_to_rgb(hex_color: str) -> tuple[int, int, int] | None:
    """
    Converts a '#rrggbb' hex color string into an (r, g, b) tuple, or None if hex_color isn't a
    valid 6-digit hex color string.
    """
    hex_color = hex_color.lstrip('#')
    if len(hex_color) != 6:
        return None
    try:
        return int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16)
    except ValueError:
        return None
