"""
Module implementing the forgot password modal component and callback registration.
"""
import dash_mantine_components as dmc
import requests
from dash import callback
from dash import html
from dash import Input
from dash import Output
from dash import State
from dash.exceptions import PreventUpdate
from dash_iconify import DashIconify
from ecodev_core import engine
from ecodev_core import logger_get
from ecodev_core import select_user
from ecodev_core import SETTINGS
from sqlmodel import Session

from ecodev_front.constants import CHILDREN
from ecodev_front.constants import INDEX
from ecodev_front.constants import N_CLICKS
from ecodev_front.constants import OPENED
from ecodev_front.constants import TYPE
from ecodev_front.constants import VALUE
from ecodev_front.ids import BUTTON
from ecodev_front.ids import FORGOT_PWD
from ecodev_front.ids import MODAL
from ecodev_front.ids import NOTIFICATION
from ecodev_front.ids import SUBMIT_BTN
from ecodev_front.ids import TEXT_INPUT

log = logger_get(__name__)

FORGOT_PWD_BTN_ID = {TYPE: FORGOT_PWD, INDEX: BUTTON}
FORGOT_PWD_MODAL_ID = {TYPE: FORGOT_PWD, INDEX: MODAL}
FORGOT_PWD_EMAIL_ID = {TYPE: FORGOT_PWD, INDEX: TEXT_INPUT}
FORGOT_PWD_SUBMIT_ID = {TYPE: FORGOT_PWD, INDEX: SUBMIT_BTN}
FORGOT_PWD_NOTIF_ID = {TYPE: FORGOT_PWD, INDEX: NOTIFICATION}

_GENERIC_SUCCESS_MSG = (
    'If this email is registered, you will receive a password reset email shortly.'
)


def attempt_reset(email: str) -> bool:
    """
    Checks user existence then triggers a password reset email via eco_auth.
    Returns True on success or unknown email (to avoid account enumeration).
    Returns False only on a technical failure (missing credentials, API error).
    """
    try:
        with Session(engine) as session:
            select_user(email, session)
    except Exception:
        log.info('Password reset requested for unknown email: %s', email)
        return True

    api_host = SETTINGS.api.host  # type: ignore[attr-defined]
    api_user = SETTINGS.api.user  # type: ignore[attr-defined]
    api_password = SETTINGS.api.password  # type: ignore[attr-defined]

    if not api_user or not api_password:
        log.warning('Service account credentials not configured — cannot trigger reset email.')
        return False

    try:
        token = (
            requests.post(
                f'{api_host}/login',
                data={'username': api_user, 'password': api_password},
            )
            .json()
            .get('access_token')
        )
        requests.get(
            f'{api_host}/reset-password?user={email}',
            headers={'Authorization': f'Bearer {token}'},
        )
    except Exception as error:
        log.error('Failed to trigger reset email for %s: %s', email, error)
        return False

    return True


def forgot_password_modal() -> dmc.Modal:
    """
    Returns the forgot password modal component.
    Rendered inside login() when with_forgot_pwd=True.
    """
    return dmc.Modal(
        id=FORGOT_PWD_MODAL_ID,
        title='Reset your password',
        centered=True,
        size='md',
        children=[
            dmc.Text(
                'Enter your email address and we will send you a reset link.',
                size='sm',
                mb='md',
            ),
            dmc.TextInput(
                id=FORGOT_PWD_EMAIL_ID,
                label='Your email address:',
                placeholder='you@example.com',
                required=True,
                leftSection=DashIconify(icon='ic:round-alternate-email'),
            ),
            dmc.Button(
                'Send reset link',
                id=FORGOT_PWD_SUBMIT_ID,
                mt='md',
                leftSection=DashIconify(icon='mdi:email-send-outline'),
            ),
            html.Div(id=FORGOT_PWD_NOTIF_ID, style={'marginTop': '10px'}),
        ],
    )


@callback(
    Output(FORGOT_PWD_MODAL_ID, OPENED),
    Input(FORGOT_PWD_BTN_ID, N_CLICKS),
    prevent_initial_call=True,
)
def open_forgot_pwd_modal(n_clicks: int) -> bool:
    """
    Opens the forgot password modal when the trigger button is clicked.
    """
    return bool(n_clicks)


@callback(
    Output(FORGOT_PWD_NOTIF_ID, CHILDREN),
    Input(FORGOT_PWD_SUBMIT_ID, N_CLICKS),
    State(FORGOT_PWD_EMAIL_ID, VALUE),
    prevent_initial_call=True,
)
def submit_forgot_password(n_clicks: int, email: str) -> dmc.Alert:
    """
    Calls attempt_reset and returns a success or error alert based on the outcome.
    """
    if not n_clicks:
        raise PreventUpdate
    if not email:
        return dmc.Alert('Please enter a valid email address.', color='red', title='Missing email')
    if not attempt_reset(email):
        return dmc.Alert(
            'A technical error occurred. Please contact your administrator.',
            color='red',
            title='Error',
        )
    return dmc.Alert(_GENERIC_SUCCESS_MSG, color='green', title='Request sent')
