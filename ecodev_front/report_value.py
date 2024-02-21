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
                dmc.Text(title, weight=700, size='16px', color='grey'),
                dmc.Text(value, weight=700, size='16px'),
                dmc.Text(unit, size='14px', italic=True),
            ]
        )
    )
