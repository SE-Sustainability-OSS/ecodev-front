import dash_mantine_components as dmc
from dash_iconify import DashIconify


def further_info(info: str | list[dmc.Text], large: bool = False) -> dmc.Tooltip:
    """
    Renders a gray info icon which opens the further info tooltip.
    """
    return dmc.Tooltip(
        label=info,
        position='top-right',
        multiline=True,
        offset=3,
        radius='md',
        color='white',
        style={'max-width': 500, 'border': '1px solid #dcdcdc'},
        closeDelay=300,
        children=[
            DashIconify(icon='material-symbols:info-outline-rounded',
                        color='gray',
                        width=28 if large else 22)
        ]
    )
