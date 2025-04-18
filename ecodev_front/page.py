"""
Module implementing a generic page object to be used throughout the app
"""
from pathlib import Path
from typing import Callable

import dash_mantine_components as dmc
from ecodev_core import Frozen

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
    def id(self) -> str:
        module_name = Path(self.module).stem.split('.')[-2].replace('_', '-')
        page_name = Path(self.module).stem.split('.')[-1].replace('_', '-')
        return f'{module_name}-{page_name}-id'

    @property
    def url(self) -> str:
        module_name = Path(self.module).stem.split('.')[-2].split('_')[-1]
        page_name = Path(self.module).stem.split('.')[-1].split('page_')[-1].replace('_', '-')
        return f'/{module_name}/{page_name}'

    @property
    def stepper_step(self) -> dmc.StepperStep:
        return stepper_step(
            label=self.title,
            description='',
            icon=self.icon,
            href=self.url,
        )
        
    @property
    def render_layout(self) -> dmc.Box:
        return self.layout(self)
