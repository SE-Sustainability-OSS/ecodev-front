"""
Module implementing the navbar login / logout components
"""
import dash_mantine_components as dmc
from dash_iconify import DashIconify

LOGIN_USERNAME_INPUT_ID = 'login-username-id'
LOGIN_PASSWORD_INPUT_ID = 'login-password-id'
LOGIN_BTN_ID = 'login-button-id'


def navbar_login(username_placeholder: str = 'Username',
                 password_placeholder: str = 'Password',
                 button_label: str = 'Login',
                 button_color: str = 'white'):
    """
    Login bar component, shown when no user-tokens have been set.
    """
    return dmc.GridCol(span=8, children=[
        dmc.Group([
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
                       style={'margin': '5px', 'width': '5vw', 'color': 'gray'})
        ], style={'display': 'flex',
                  'justifyContent': 'center',
                  'alignItems': 'center',
                  'textAlign': 'center'})
    ])
