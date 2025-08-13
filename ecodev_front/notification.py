from ecodev_front import dash_icon
from ecodev_front.constants import ACTION
from ecodev_front.constants import COLOR
from ecodev_front.constants import ICON
from ecodev_front.constants import ID
from ecodev_front.constants import MESSAGE
from ecodev_front.constants import TITLE
from ecodev_front.constants import WITH_CLOSE_BUTTON


def send_notification(title: str,
                      message: str,
                      icon: str | None = None,
                      color: str | None = None,
                      with_close_button: bool = True,
                      notif_id: str | None = None,
                      **kwargs,
                      ):
    """
    Returns a list of dict to be sent to the SEND_NOTIFICATION component

    Args:
        with_close_button (bool): Adds a close button to the notification div
        notif_id (Optional[str]): Notification ID. If None, then uses title. Defaults \
            to None.
    """
    icon = icon or ('ic:round-celebration' if title == 'Success' else
                    'icon-park-outline:link-cloud-faild' if title == 'Failure' else '')
    color = color or ('green' if title == 'Success' else 'red' if title == 'Failure' else 'gray')
    return [{TITLE: title,
             ID: notif_id or f'notif-id-{title}',
             ACTION: 'show',
             MESSAGE: message,
             ICON: dash_icon(icon=icon),
             COLOR: color,
             WITH_CLOSE_BUTTON: with_close_button,
             **kwargs,
             }]
