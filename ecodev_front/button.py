from enum import Enum
from enum import unique

import dash_mantine_components as dmc

from ecodev_front.constants import INDEX
from ecodev_front.constants import TYPE
from ecodev_front.icon import dash_icon
from ecodev_front.ids import ADD_BTN
from ecodev_front.ids import CANCEL_BTN
from ecodev_front.ids import CLOSE_BTN
from ecodev_front.ids import CONFIRM_BTN
from ecodev_front.ids import CONTINUE_BTN
from ecodev_front.ids import DELETE_BTN
from ecodev_front.ids import SAVE_BTN
from ecodev_front.ids import UPDATE_BTN


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


@unique
class ButtonAction(str, Enum):
    """
    Enum listing the different actions that can be done with a button
    """
    CONFIRM = 'Confirm'
    CLOSE = 'Close'
    DELETE = 'Delete'
    SAVE = 'Save'
    CANCEL = 'Cancel'
    UPDATE = 'Update'
    ADD = 'Add'
    CONTINUE = 'Continue'


ACTION_TO_ICON: dict[ButtonAction, str] = {
    ButtonAction.CONFIRM: 'lsicon:submit-outline',
    ButtonAction.CLOSE: 'healthicons:no-outline',
    ButtonAction.DELETE: 'solar:trash-bin-trash-outline',
    ButtonAction.SAVE: 'material-symbols-light:file-save-rounded',
    ButtonAction.CANCEL: 'nonicons:not-found-16',
    ButtonAction.UPDATE: 'hugeicons:location-update-01',
    ButtonAction.ADD: 'material-symbols-light:group-add-rounded',
    ButtonAction.CONTINUE: 'codicon:debug-continue'
}

ACTION_TO_COLOR: dict[ButtonAction, str] = {
    ButtonAction.CONFIRM: 'green.9',
    ButtonAction.CLOSE: 'gray',
    ButtonAction.DELETE: 'red.9',
    ButtonAction.SAVE: 'blue.9',
    ButtonAction.CANCEL: 'red.5',
    ButtonAction.UPDATE: 'blue.5',
    ButtonAction.ADD: 'green.5',
    ButtonAction.CONTINUE: 'blue.7'
}

ACTION_TO_ID = {
    ButtonAction.CONFIRM: CONFIRM_BTN,
    ButtonAction.CLOSE: CLOSE_BTN,
    ButtonAction.DELETE: DELETE_BTN,
    ButtonAction.SAVE: SAVE_BTN,
    ButtonAction.CANCEL: CANCEL_BTN,
    ButtonAction.UPDATE: UPDATE_BTN,
    ButtonAction.ADD: ADD_BTN,
    ButtonAction.CONTINUE: CONTINUE_BTN
}


def render_action_button(index: str,
                         action: ButtonAction,
                         label: str | None = None,
                         color: str | None = None,
                         display: str = 'inline-block',
                         variant: str = 'outline'):
    """
    Renders a button to go on to the next step
    """
    return dmc.Button(
        children=label or action,
        id={TYPE: ACTION_TO_ID[action], INDEX: index},
        color=color or ACTION_TO_COLOR.get(action) or 'blue.7',
        leftSection=dash_icon(ACTION_TO_ICON[action]),
        display=display,
        variant=variant,
    )
