"""
Module implementing a generic module object to be used throughout the app
"""
from pathlib import Path
from typing import Callable

import dash_mantine_components as dmc
from dash import html
from ecodev_core import Frozen
from ecodev_core import logger_get

from ecodev_front.nav_items import action_item
from ecodev_front.page import Page
from ecodev_front.shadow_button import module_main_button

log = logger_get(__name__)


class Module(Frozen):
    """
    Class representing an application module.

    Attributes
    ----------
    file: str
        The file path of the module. Provided by __name__ where the module_def or __init__.py file
        are located. This will define the module id and url (e.g. if the module dir is named
        'module_test', the module id will be 'module-test' and the module url will be '/test').)

    name: str
        The name of the module. This format will be used on front-end display (e.g. 'Test')

    icon: str
        An icon to represent the module.

    pages: list[Page]
        The list of the module's pages. They can be registered after the module has been defined.
        At least one page must be defined per module to avoid breaking functionalities
        (e.g. header icon)

    navbar_layout: Callable
        A function which renders the navbar content for this module.


    main_page_button_kwargs: dict = {}
        Dictionary containing the kwargs of the module_main_button function.
        Optional. Use to override default proposed values

    protected: bool
        If the module is protected, the user must be authenticated to access it. Default is True.

    admin: bool
        If the module is admin, only users with admin privileges can access it. Default is False.

    Properties
    ----------
    id: str
        The module id, derived from the module directory name.

    url: str
        The module url, derived from the module directory name.

    header_icon: html.Div
        An icon which can be used in the header of an app, for quick navigation to the module's
        first page. As such, the order in which the pages are added to the module's pages is
        relevant.

    module_navbar: dmc.Stack
        A styled navbar for the module, containing a stepper of the pages of the module.
    """
    file: str

    name: str
    icon: str

    pages: list[Page]
    navbar_layout: Callable

    main_page_button_kwargs: dict = {}

    protected: bool = True
    admin: bool = False

    @property
    def id(self) -> str:
        return Path(self.file).stem.split('.')[-1]

    @property
    def url(self) -> str:
        return f"/{Path(self.file).stem.split('.')[-1]}"

    @property
    def header_icon(self) -> html.Div:
        """
        Returns a header icon for the module.
        """
        return action_item(
            id=self.id,
            icon=self.icon,
            label=self.name.capitalize(),
            href=self.pages[0].url,
        )

    def render_navbar(self, **kwargs) -> dmc.Stack:
        """
        Renders the module's navbar from the navbar layout function provided.
        """
        return self.navbar_layout(self, **kwargs)

    def render_main_page_button(self):
        """
        Renders the main module's button.
        You can pass custom module_main_button args when creating the module through the
        main_page_button_kwargs dict.
        """
        default_kwargs = {
            'id': self.id,
            'label_top': 'View',
            'label_bottom': self.name.capitalize(),
            'icon': self.icon,
            'color': '#0066a1'
        } | self.main_page_button_kwargs

        return module_main_button(**default_kwargs)
