"""
BLA
"""
from typing import Optional

import dash_mantine_components as dmc
from dash import html

from ecodev_front.display_utils import number_formatting


def report_value(title: str, value: str | int, unit: Optional[str] = None) -> html.Div:
    """
    BLA
    """
    if isinstance(value, (int, float)):
        value = number_formatting(value)
    elif value.isnumeric():
        value = number_formatting(float(value))

    return html.Div(
        dmc.Group(
            [
                dmc.Text(title, fw=700, fz='16px', c='grey'),
                dmc.Text(value, fw=700, fz='16px'),
                dmc.Text(unit, fz='14px', fs='italic'),
            ]
        )
    )
