"""
Module implementing a generic page object to be used throughout the app
"""
from dash import register_page
from ecodev_core import Frozen

from ecodev_front.page_header import page_header
from ecodev_front.stepper import stepper_step


class Page(Frozen):
    """
    Class representing an application page.
    """
    id: str
    url: str

    name: str
    icon: str

    title: str
    description: str = ''

    protected: bool = True
    admin: bool = False

    @property
    def base_layout(self):
        """
        Returns a basic layout for the page.
        """
        return [page_header(self.id, self.title, self.icon, self.description)]

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
