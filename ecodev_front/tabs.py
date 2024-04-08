"""
Module to render the tabs element (composed of different individual dmc.Tab element)
"""
from typing import List

import dash_mantine_components as dmc


def tabs(tabs_list: List[dmc.Tab], tabs_id: str, value: str) -> dmc.Tabs:
    """
    Renders a dmc.Tabs components
    """
    return dmc.Tabs(children=[dmc.TabsList(tabs_list)], id=tabs_id, value=value)


def tab(value: str):
    """
    Renders a dmc.Tab component
    """
    return dmc.Tab(' '.join(value.split('_')).capitalize(), value=value)
