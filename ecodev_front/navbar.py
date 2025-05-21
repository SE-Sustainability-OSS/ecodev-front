"""
File containing a module navbar component for an app.
"""
import dash_mantine_components as dmc
from dash_iconify import DashIconify

from ecodev_front.divider import divider
from ecodev_front.module import Module
from ecodev_front.page import Page
from ecodev_front.stepper import vertical_stepper
from ecodev_front.text import section_title


def icon_navbar(module: Module,
                pages: list[Page],
                active_page: int,
                ) -> dmc.Stack:
    """
    Renders a short module navbar, with an action icon for each page.
    """
    return dmc.Stack([
        dmc.Stack([
            dmc.Tooltip(
                DashIconify(icon=module.icon, color='#cdcdcd', width=44),
                label=f'{module.name.capitalize()} Module',
                position='bottom',
                color='gray',
                transitionProps={
                    'transition': 'slide-down',
                    'duration': 200,
                    'timingFunction': 'ease'
                },
            )
        ], align='center', mt=5, mb=0),
        divider(margin=0, color='lightgray'),
        dmc.ScrollArea(
            dmc.Stack([
                page.navbar_icon(active=active_page == idx)
                for idx, page in enumerate(pages)], gap='2vh'),
            h='90vh', mt=20,
        )
    ], p=10)


def stepper_navbar(module: Module,
                   steps: list[dmc.StepperStep],
                   active_step: int = 0
                   ) -> dmc.Stack:
    """
    Renders a navbar with a module title and a vertical stepper step embedded in a scrollable area.
    """
    return dmc.Stack([
        dmc.Group([
            DashIconify(icon=module.icon, color='gray', width=28),
            section_title(module.name.capitalize(), c='dimmed'),
        ], align='center', mt=5, mb=10, gap=10),
        divider(margin=0, color='lightgray'),
        dmc.ScrollArea(
            vertical_stepper(
                id=f'{module.id}-stepper',
                steps=steps,
                active_step=active_step
            ),
            h='80vh', mt=10,
        )
    ], p=20)
