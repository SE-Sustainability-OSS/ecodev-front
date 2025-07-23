import dash_mantine_components as dmc

from ecodev_front.constants import INDEX
from ecodev_front.constants import TYPE
from ecodev_front.icon import dash_icon
from ecodev_front.ids import BUTTON
from ecodev_front.ids import COLUMN
from ecodev_front.ids import CONTINUE
from ecodev_front.ids import SAVE
from ecodev_front.ids import USE


def button(id: str | dict,
           text: str,
           icon: str,
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
        leftSection=dash_icon(icon),
        fullWidth=full_width,
        w=w
    )


def render_continue_button(index: str, display: str = 'none'):
    """
    Renders a button to go on to the next step
    """
    return dmc.Button(
        'Continue',
        id={TYPE: BUTTON, INDEX: index, USE: CONTINUE},
        color='blue.7',
        leftSection=dash_icon('codicon:debug-continue'),
        display=display
    )


def render_save_button(index: str,
                       col: str = '',
                       width: str | int = '50%'):
    """
    Renders a button to save information
    """
    return dmc.Button(
        'Save',
        id={TYPE: BUTTON, INDEX: index, USE: SAVE, COLUMN: col},
        color='blue',
        leftSection=dash_icon('humbleicons:chevron-right'),
        w=width,
        variant='outline'
    )
