from ecodev_front import dash_icon
from ecodev_front.constants import ACTION
from ecodev_front.constants import COLOR
from ecodev_front.constants import ICON
from ecodev_front.constants import MESSAGE
from ecodev_front.constants import TITLE


def send_notification(title: str,
                      message: str,
                      icon: str | None = None,
                      color: str | None = None):
    """
    Returns a list of dict to be sent to the SEND_NOTIFICATION component
    """
    icon = icon or 'ic:round-celebration' if title == 'Success' else \
        'icon-park-outline:link-cloud-faild' if title == 'Failure' else ''
    color = color or 'green' if title == 'Success' else 'red' if title == 'Failure' else 'gray'
    return [{TITLE: title,
             ACTION: 'show',
             MESSAGE: message,
             ICON: dash_icon(icon=icon),
             COLOR: color}]
