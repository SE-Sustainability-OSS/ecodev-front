"""
Module implementing segmented control
"""
import dash_mantine_components as dmc

from ecodev_front.constants import INDEX, TYPE, VALUE
from ecodev_front.ids import SWITCH
from ecodev_front.text import label_text


def switch(id: str,
           data: dict[str, str],
           value: str | None = None,
           label: str = '',
           color: str = 'blue.7',
           bg: str = 'white',
           size: str = 'sm',
           style: dict = {},
           label_kwargs: dict = {},
           **kwargs
           ) -> dmc.SegmentedControl:
    """
    Renders a switch select component
    """
    switch = dmc.SegmentedControl(
        id={TYPE: SWITCH, INDEX: id},
        value=value if value else data[0][VALUE],
        data=data,
        color=color,
        size=size,
        persistence=True,
        persistence_type='session',
        style=style or {'backgroundColor': bg, 'border': '1px solid #dcdcdc'},
        **kwargs
    )
    if not label:
        return switch
    
    return dmc.Stack([label_text(label, **label_kwargs), switch], gap='0px')
