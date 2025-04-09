"""
Module implementing a generic page object to be used throughout the app
"""
import dash_mantine_components as dmc
from dash_iconify import DashIconify
from ecodev_core import Basic

from ecodev_front.divider import divider
from ecodev_front.page import Page
from ecodev_front.stepper import vertical_stepper


class Module(Basic):
    """
    Class representing an application module.
    """
    id: str
    url: str

    name: str
    icon: str

    pages: list[Page] = []

    protected: bool = True
    admin: bool = False

    def navbar(self, active_step: int = 0):
        """
        Returns a styled navbar for the module.
        """
        return dmc.Stack([
            dmc.Group([
                DashIconify(icon=self.icon, color='gray', width=24),
                dmc.Title(self.name, fz=20, fw=700, c='dimmed', ta='left'),
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
