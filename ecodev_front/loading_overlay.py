import dash_mantine_components as dmc


def loading_overlay(id: str | dict, color: str = '#f2f2f2'):
    """
    Renders a loading overlay
    """
    return dmc.LoadingOverlay(
        visible=False,
        id=id,
        overlayProps={'radius': 'sm', 'blur': 2, 'color': color},
        zIndex=10
    )
