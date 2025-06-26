import dash_mantine_components as dmc
from dash_iconify import DashIconify


def further_info(
    info: str | list[dmc.Text], 
    large: bool = False, 
    **kwargs
) -> dmc.Tooltip:
    """
    Renders a gray info icon which opens the further info tooltip.
    """
    kwargs.setdefault("position", "top-right")
    kwargs.setdefault("multiline", True)
    kwargs.setdefault("offset", 3)
    kwargs.setdefault("radius", "md")
    kwargs.setdefault("closeDelay", 300)
    kwargs.setdefault("color", "white")
    kwargs.setdefault("style", {"max-width": 500, "border": "1px solid #dcdcdc"})

    return dmc.Tooltip(
        label=dmc.Text(info, c='black') if isinstance(info, str) else info,
        children=[
            DashIconify(
                icon="material-symbols:info-outline-rounded",
                color="gray",
                width=28 if large else 22,
            )
        ],
        **kwargs
    )
