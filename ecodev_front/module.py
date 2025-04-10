"""
Module implementing a generic module object to be used throughout the app
"""
from pathlib import Path

from ecodev_core import Basic

from ecodev_front.nav_items import action_item
from ecodev_front.navbar import navbar
from ecodev_front.page import Page


class Module(Basic):
    """
    Class representing an application module.
    """
    file: str

    name: str
    icon: str

    pages: list[Page] = []

    protected: bool = True
    admin: bool = False

    @property
    def id(self):
        return Path(self.file).stem.split('.')[-1]

    @property
    def url(self):
        return f"/{Path(self.file).stem.split('.')[-1]}"

    @property
    def header_icon(self):
        """
        Returns a header icon for the module.
        """
        return action_item(
            id=self.id,
            icon=self.icon,
            label=self.name.capitalize(),
            href=self.pages[0].url,
        )

    def module_navbar(self, active_step: int = 0):
        """
        Returns a styled navbar for the module.
        """
        return navbar(
            id=self.id,
            name=self.name,
            icon=self.icon,
            steps=[page.stepper_step for page in self.pages],
            active_step=active_step
        )
