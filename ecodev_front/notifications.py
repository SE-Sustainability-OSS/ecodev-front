"""
Module containing the different notifications used in the app

TODO: write example in ecodev-app
"""
import dash_mantine_components as dmc
from dash_iconify import DashIconify


VALIDATION_NOTIF_ID = 'validation-notif-id'
LOADING_ERROR_NOTIF_ID = 'loading-error-notif-id'
LOADING_INFO_NOTIF_ID = 'loading-info-notif-id'
SAVE_NOTIF_ID = 'save-notif-id'


def get_launch_notif(title_name: str) -> dmc.Notification:
    """
    Generate a 'launch' notification
    """
    return dmc.Notification(
        id=f'notif_{title_name}_id',
        title=f'{title_name} - initiated',
        message='The process has started',
        loading=True,
        color='orange',
        action='show',
    )


def get_error_notif(title_name: str, raw_msg: str) -> dmc.Notification:
    """
    Generate an 'error' notification
    """
    msg = raw_msg
    if len(raw_msg) > 50:
        top_msg = raw_msg.lstrip()[:50]
        msg = dmc.Stack([
            top_msg,
            dmc.Popover(
                children=[
                    dmc.PopoverTarget(dmc.Button('More details...')),
                    dmc.PopoverDropdown(
                        dmc.Textarea(
                            raw_msg,
                            autosize=True,
                            w=500,
                            disabled=True
                        )
                    ),
                ]
            )
        ])
    return dmc.Notification(
        id=f'notif_{title_name}_error_id',
        title=f"Error in '{title_name}'",
        message=msg,
        loading=False,
        color='red',
        action='show',
        autoClose=False,
        icon=DashIconify(icon='codicon:error'),
    )


def get_info_notif(title_name: str, msg: str) -> dmc.Notification:
    """
    Generate an 'info' notification
    """
    return dmc.Notification(
        id=f'notif_{title_name}_info_id',
        title=f'{title_name} - info',
        message=msg,
        loading=False,
        color='blue',
        action='show',
        autoClose=2000,
    )


def get_complete_notif(
        title_name: str, notif_id: str | None = None,
        message: str | None = None, autoclose: int | None = None
) -> dmc.Notification:
    """
    Generate a 'process complete' notification
    """
    notif_id = notif_id or f'notif_{title_name}_id'
    message = message or 'The process is now complete'
    autoclose = autoclose or 2000

    return dmc.Notification(
        id=notif_id,
        title=f'{title_name} - complete',
        message=message,
        loading=False,
        color='green',
        action='show',
        autoClose=autoclose,
        icon=DashIconify(icon='akar-icons:circle-check'),
    )
