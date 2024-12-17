import dash_mantine_components as dmc


def loading_overlay(id: str):
    """
    Renders a loading overlay
    """
    return dmc.LoadingOverlay(
        visible=False,
        id=id,
        overlayProps={'radius': 'sm', 'blur': 2},
        zIndex=10
    )
