"""
Module implementing a generic page wrapper to handle authentication
"""
from typing import Dict
from typing import List
from typing import Union

import dash_mantine_components as dmc
from dash import html
from ecodev_core import get_access_token
from ecodev_core import get_user
from ecodev_core import Permission

NOT_AUTHORIZED = [html.P('Unauthorized. Please login to access')]


def generic_page(
    token: Dict, page: Union[dmc.Stack, List], admin: bool = False
) -> Union[dmc.Stack, List]:
    """
    Returns a NOT_AUTHORIZED if the token is not filled or if the user is not authorized to connect.
    If admin is True, the client is only authorized to see passed page if he has admin privileges.
    """
    if not (user := get_user(get_access_token(token))):
        return NOT_AUTHORIZED

    return (
        page if (not admin or user.permission == Permission.ADMIN) else NOT_AUTHORIZED
    )
