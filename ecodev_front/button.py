import dash_mantine_components as dmc
from dash_iconify import DashIconify


def button(id: str,
           text: str,
           icon: DashIconify,
           variant: str = 'filled',
           color: str = 'default-color',
           full_width: bool = True,
           w: int | None = None):
    """
    Function to render a button
    - id: unique identifier for the button
    - text: text displayed on the button
    - icon: icon displayed on the left side of the button
    - variant: ('subtle', 'gradient', 'filled', 'light', 'outline') format of the button
    - color: color of the button
    - full_width: whether the button should take up full width of its parent container
    - w: width of the button in pixels (optional)
    """
    return dmc.Button(
        children=text,
        id=id,
        color=color,
        variant=variant,
        leftSection=icon,
        fullWidth=full_width,
        w=w
    )
