"""
Module implementing a generic page object to be used throughout the app
"""
from pathlib import Path
from typing import Callable

import dash_mantine_components as dmc
from dash import register_page
from ecodev_core import Frozen

from ecodev_front.navbar_page_icon import navbar_page_icon
from ecodev_front.stepper import stepper_step


class Page(Frozen):
    """
    Class representing an application page.

    Attributes
    ----------
    file: str
        The file path of the module. Provided by __name__ where the module_def or __init__.py file
        are located. This will define the module id and url (e.g. if the module dir is named
        'module_test', the module id will be 'module-test' and the module url will be '/test').)

    name: str
        The name of the module. Keep it to short form as it is used in page ID and URL

    icon: str
        An icon to represent the module.

    title: str
        The title of the page. This will be displayed in the header and the navbar.

    description: str (optional)
        A description of the page. This will be displayed in the page header. Defaults to
        empty string.

    protected: bool
        If the module is protected, the user must be authenticated to access it. Default is True.

    admin: bool
        If the module is admin, only users with admin privileges can access it. Default is False.

    Properties
    ----------
    id: str
        The page's id, derived from the module and page directory name.

    url: str
        The page's url, derived from the module and page directory name.

    stepper_step: dmc.StepperStep
        Returns a stepper step for the page, to be used in the module navbar.
    """
    module: str

    name: str
    icon: str
    title: str
    description: str

    layout: Callable
    aside: Callable | None = None

    protected: bool = True
    admin: bool = False

    @property
    def module_name(self) -> str | None:
        if (name := Path(self.module).stem.split('.')[-2].replace('_', '-')) == 'pages':
            return None
        return name

    @property
    def page_name(self) -> str:
        return Path(self.module).stem.split('.')[-1].split('page_')[-1].replace('_', '-')

    @property
    def id(self) -> str:
        if self.module_name:
            return f'{self.module_name}-{self.page_name}-id'
        return f'{self.page_name}-id'

    @property
    def url(self) -> str:
        if self.module_name:
            return f'/{self.module_name}/{self.page_name}'
        if self.page_name == 'main':
            return '/'
        return f'/{self.page_name}'

    @property
    def stepper_step(self) -> dmc.StepperStep:
        return stepper_step(
            label=self.title,
            description=self.description,
            icon=self.icon,
            href=self.url,
        )

    def navbar_icon(self, active) -> dmc.Anchor:
        return navbar_page_icon(self.icon, self.title, self.url, active)

    def register(self, *args, **kwargs):
        """
        Register the page in the app
        """
        register_page(
            module=self.module,
            path=self.url,
            title=self.title,
            layout=self.layout(self)
        )
