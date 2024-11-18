"""
Module implementing a stepper and stepper-step components
"""
from typing import Dict

import dash_mantine_components as dmc
from dash_iconify import DashIconify


def vertical_stepper(id: str,
                     steps: list[dmc.StepperStep],
                     color: str = '#0066a1',
                     style: Dict | None = None
                     ) -> dmc.Stepper:
    """
    Returns a vertical stepper.
    """
    return dmc.Stepper(
        id=id,
        active=0,
        orientation='vertical',
        color=color,
        children=steps,
        style=style
    )


def stepper_step(label: str,
                 icon: str,
                 description: str | None = None,
                 href: str | None = None
                 ) -> dmc.StepperStep:
    """
    Returns a stepper step with redirecting icons, if provided with an href.
    """
    icon = DashIconify(icon=icon, width=22)
    active_step = dmc.Anchor(icon, href=href, c='#495057', inline=True) if href else icon
    completed_step = dmc.Anchor(icon, href=href, c='white', inline=True) if href else icon

    return dmc.StepperStep(
        label=dmc.NavLink(label=label, description=description, href=href,
                          rightSection=None, active=False, style={'margin-top': '-10px'}),
        icon=active_step,
        completedIcon=completed_step,
        fz=18
    )
