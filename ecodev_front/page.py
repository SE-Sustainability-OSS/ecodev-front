"""
Module implementing a generic page object to be used throughout the app
"""
from pathlib import Path

from dash import register_page
from ecodev_core import Frozen

from ecodev_front.page_layout import page_layout
from ecodev_front.stepper import stepper_step


class Page(Frozen):
    """
    Class representing an application page.
    """
    file: str

    name: str
    icon: str

    title: str
    description: str = ''

    protected: bool = True
    admin: bool = False

    @property
    def id(self):
        module_name = Path(self.file).stem.split('.')[-2].replace('_', '-')
        page_name = Path(self.file).stem.split('.')[-1].replace('_', '-')
        return f'{module_name}-{page_name}'

    @property
    def url(self):
        module_name = Path(self.file).stem.split('.')[-2].split('_')[-1]
        return f'/{module_name}/{self.name}'

    @property
    def base_layout(self):
        """
        Returns a basic layout for the page.
        """
        return [page_layout(self.id, self.title, self.icon, self.description)]

    def register(self, file: str):
        """
        Registers the page with Dash
        """
        register_page(
            module=file,
            path=self.url,
            title=self.title,
            layout=self.base_layout
        )

    @property
    def stepper_step(self):
        return stepper_step(
            label=self.title,
            description='',
            icon=self.icon,
            href=self.url,
        )
