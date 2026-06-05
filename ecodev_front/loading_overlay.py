import dash_mantine_components as dmc

from ecodev_front.constants import INDEX
from ecodev_front.constants import MAIN_DM_COLOR
from ecodev_front.constants import TYPE
from ecodev_front.constants import VERY_LIGHT_GRAY
from ecodev_front.ids import LOADING_OVERLAY


def loading_overlay(id: str | dict,
                    color: str = MAIN_DM_COLOR,
                    bg_color: str = VERY_LIGHT_GRAY,
                    zIndex=10,
                    loader_props: dict | None = None,
                    overlay_props: dict | None = None,
                    transition_props: dict | None = None):
    """
    Renders a loading overlay.
    Default prop values are:
    - loader_props: {'color': color, 'size': 'sm'}
    - transition_props: {'transition': 'fade', 'duration': 1_000}
    - overlay_props: {'radius': 'sm', 'blur': 2, 'color': bg_color}
    """
    return dmc.LoadingOverlay(
        visible=False,
        id=id if isinstance(id, dict) else {TYPE: LOADING_OVERLAY, INDEX: id},
        loaderProps=loader_props or {'color': color, 'size': 'sm'},
        transitionProps=transition_props or {'transition': 'fade', 'duration': 1_000},
        overlayProps=overlay_props or {'radius': 'sm', 'blur': 2, 'color': bg_color},
        zIndex=zIndex
    )
