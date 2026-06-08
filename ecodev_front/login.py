"""
Module implementing the navbar login / logout components
"""
from typing import Union

import dash_mantine_components as dmc
from dash import html
from dash_iconify import DashIconify

from ecodev_front.constants import INDEX
from ecodev_front.constants import TYPE
from ecodev_front.forgot_password import forgot_password_modal
from ecodev_front.forgot_password import FORGOT_PWD_BTN_ID
from ecodev_front.ids import BUTTON
from ecodev_front.ids import LOGIN
from ecodev_front.ids import LOGIN_BTN_ID
from ecodev_front.ids import LOGIN_PASSWORD_INPUT_ID
from ecodev_front.ids import LOGIN_USERNAME_INPUT_ID
from ecodev_front.ids import PASSWORD
from ecodev_front.ids import USERNAME


def login(username_placeholder: str = 'Username',
          password_placeholder: str = 'Password',
          button_label: str = 'Login',
          button_color: str = 'white',
          with_forgot_pwd: bool = False,
          ) -> Union[dmc.Group, html.Div]:
    """
    Login bar component, shown when no user-tokens have been set.
    When with_forgot_pwd=True, appends a 'Forgot password?' button and the reset modal.
    """
    _login_btn_style = {'margin': '5px', 'width': '5vw', 'color': 'gray'}
    forgot_btn = dmc.Button(
        'Forgot password?',
        id=FORGOT_PWD_BTN_ID,
        radius='xl',
        variant='subtle',
        color='gray',
        style={'margin': '5px', 'color': 'white'},
    ) if with_forgot_pwd else None

    login_group = dmc.Group(
        [
            dmc.TextInput(id=LOGIN_USERNAME_INPUT_ID,
                          placeholder=username_placeholder,
                          radius='xl',
                          style={'width': '15vw'},
                          leftSection=DashIconify(icon='material-symbols:supervised-user-circle')),
            dmc.PasswordInput(id=LOGIN_PASSWORD_INPUT_ID,
                              placeholder=password_placeholder,
                              radius='xl',
                              style={'width': '15vw'},
                              leftSection=DashIconify(icon='bi:shield-lock')),
            dmc.Button(button_label,
                       id=LOGIN_BTN_ID,
                       radius='xl',
                       variant=button_color,
                       style=_login_btn_style),
            forgot_btn,
        ],
        style={'display': 'flex',
               'justifyContent': 'center',
               'alignItems': 'center',
               'textAlign': 'center'},
    )

    if not with_forgot_pwd:
        return login_group

    return html.Div([login_group, forgot_password_modal()])


def login_card(username_placeholder: str = 'Username',
               password_placeholder: str = 'Password',
               button_label: str = 'Login',
               ) -> dmc.Stack:
    """
    Login card component, shown when no user-tokens have been set.
    """
    return dmc.Stack([
        username_input(username_placeholder),
        password_input(password_placeholder),
        login_button(button_label)
    ], align='center', w='15vw')


def username_input(username_placeholder: str) -> dmc.TextInput:
    """
    Renders the username input component
    """
    return dmc.TextInput(id={TYPE: LOGIN, INDEX: USERNAME},
                         placeholder=username_placeholder,
                         radius='xl',
                         w='100%',
                         leftSection=DashIconify(icon='material-symbols:supervised-user-circle'))


def password_input(password_placeholder: str) -> dmc.PasswordInput:
    """
    Renders the password input component
    """
    return dmc.PasswordInput(id={TYPE: LOGIN, INDEX: PASSWORD},
                             placeholder=password_placeholder,
                             radius='xl',
                             w='100%',
                             leftSection=DashIconify(icon='bi:shield-lock'))


def login_button(button_label: str) -> dmc.Button:
    """
   Renders the login button
   """
    return dmc.Button(button_label, id={TYPE: LOGIN, INDEX: BUTTON}, fullWidth=True)
