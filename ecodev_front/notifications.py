"""
Module containing the different notifications used in the app

TODO: write example in ecodev-app
"""
from ecodev_front.notification import send_notification


VALIDATION_NOTIF_ID = 'validation-notif-id'
LOADING_ERROR_NOTIF_ID = 'loading-error-notif-id'
LOADING_INFO_NOTIF_ID = 'loading-info-notif-id'
SAVE_NOTIF_ID = 'save-notif-id'


def get_launch_notif(title_name: str) -> list[dict]:
    """
    Generate a 'launch' notification
    """
    return send_notification(
        title=f'{title_name} - initiated',
        message='The process has started',
        notif_id=f'notif_{title_name}_id',
        color='orange',
        loading=True,
    )


def get_error_notif(title_name: str, raw_msg: str) -> list[dict]:
    """
    Generate an 'error' notification
    """
    return send_notification(
        title=f"Error in '{title_name}'",
        message=raw_msg,
        notif_id=f'notif_{title_name}_error_id',
        color='red',
        loading=False,
        autoClose=False,
        icon='codicon:error',

    )


def get_info_notif(title_name: str, msg: str) -> list[dict]:
    """
    Generate an 'info' notification
    """
    return send_notification(
        title=f'{title_name} - info',
        message=msg,
        notif_id=f'notif_{title_name}_info_id',
        color='blue'
    )


def get_complete_notif(
        title_name: str, notif_id: str | None = None,
        message: str | None = None,
        **kwargs,
) -> list[dict]:
    """
    Generate a 'process complete' notification
    """
    notif_id = notif_id or f'notif_{title_name}_id'
    message = message or 'The process is now complete'

    return send_notification(
        title=f'{title_name} - complete',
        message=message,
        notif_id=notif_id,
        icon='akar-icons:circle-check',
        color='green'
    )
