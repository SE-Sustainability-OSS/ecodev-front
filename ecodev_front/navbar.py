"""
File containing a module navbar component for an app.
"""
import dash_mantine_components as dmc
from dash_iconify import DashIconify

from ecodev_front.divider import divider
from ecodev_front.stepper import vertical_stepper
from ecodev_front.text import section_header


def navbar(id: str,
           name: str,
           icon: str,
           steps: list[dmc.StepperStep],
           active_step: int = 0
           ) -> dmc.Stack:
    """
    Renders a navbar with a module title and a vertical stepper step embedded in a scrollable area.
    """
    return dmc.Stack([
        dmc.Group([
            DashIconify(icon=icon, color='gray', width=28),
            section_header(name, c='dimmed'),
        ], align='center', mt=10, mb=10, gap=10),
        divider(margin=0, color='lightgray'),
        dmc.ScrollArea(
            vertical_stepper(
                id=id,
                steps=steps,
                active_step=active_step
            ),
            h='80vh', mt=10,
        )
    ], p=20)
