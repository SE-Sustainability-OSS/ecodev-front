"""
Module implementing a generic page object to be used throughout the app
"""
from pathlib import Path

import dash_mantine_components as dmc
from dash_iconify import DashIconify
from ecodev_core import Basic

from ecodev_front.divider import divider
from ecodev_front.nav_items import action_item
from ecodev_front.page import Page
from ecodev_front.stepper import vertical_stepper


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

    def navbar(self, active_step: int = 0):
        """
        Returns a styled navbar for the module.
        """
        return dmc.Stack([
            dmc.Group([
                DashIconify(icon=self.icon, color='gray', width=24),
                dmc.Title(self.name.capitalize(), fz=20, fw=700, c='dimmed', ta='left'),
            ], align='center', mt=10, mb=10),
            divider(margin=0, color='lightgray'),
            dmc.ScrollArea(
                vertical_stepper(
                    id=self.id,
                    color='default-color',
                    steps=[page.stepper_step for page in self.pages],
                    active_step=active_step
                ),
                h='80vh', mt=10,
            )
        ], p=20)
