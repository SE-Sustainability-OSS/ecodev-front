"""
Module implementing a stepper and stepper-step components
"""
from typing import Dict

import dash_mantine_components as dmc
from dash_iconify import DashIconify

from ecodev_front.constants import INDEX
from ecodev_front.constants import TYPE

STEPPER_ID = 'stepper-id'


def vertical_stepper(id: str,
                     steps: list[dmc.StepperStep],
                     active_step: int = 0,
                     color: str = '#0066a1',
                     style: Dict | None = None,
                     allow_next_steps_select: bool = True
                     ) -> dmc.Stepper:
    """
    Returns a vertical stepper.
    """
    return dmc.Stepper(
        id={TYPE: STEPPER_ID, INDEX: id},
        active=active_step,
        orientation='vertical',
        color=color,
        children=steps,
        style=style,
        allowNextStepsSelect=allow_next_steps_select,
        radius='lg',
    )


def stepper_step(label: str,
                 icon: str,
                 description: str | None = None,
                 href: str | None = None,
                 allow_step_click: bool = True
                 ) -> dmc.StepperStep:
    """
    Returns a stepper step with redirecting icons, if provided with an href.
    """
    icon = DashIconify(icon=icon, width=22)
    active_step = dmc.Anchor(icon, href=href, c='#0066a1', inline=True) if href else icon
    completed_step = dmc.Anchor(icon, href=href, c='white', inline=True) if href else icon

    return dmc.StepperStep(
        label=dmc.NavLink(label=label, description=description, href=href,
                          rightSection=None, active=False, p=-10 if description else 0),
        icon=active_step,
        completedIcon=completed_step,
        allowStepClick=allow_step_click,
        fz=18,
    )
