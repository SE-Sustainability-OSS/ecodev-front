import dash_mantine_components as dmc
from dash_iconify import DashIconify


def further_info(
    info: str | list[dmc.Text], 
    large: bool = False, 
    position: str = "top-right",
    multiline: bool= True,
    offset: int=3,
    radius: str= "md",
    closeDelay: int = 300,
    color: str = "white",
    style: dict = {"max-width": 500, "border": "1px solid #dcdcdc"},
    **kwargs
) -> dmc.Tooltip:
    """
    Renders a gray info icon which opens the further info tooltip.
    """

    return dmc.Tooltip(
        label=dmc.Text(info, c='black') if isinstance(info, str) else info,
        children=[
            DashIconify(
                icon="material-symbols:info-outline-rounded",
                color="gray",
                width=28 if large else 22,
            )
        ],
        position=position,
        multiline=multiline,
        offset=offset,
        radius=radius,
        closeDelay=closeDelay,
        color=color,
        style=style,
        **kwargs
    )
