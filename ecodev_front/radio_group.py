"""
Module implementing a radio group select component
"""
import dash_mantine_components as dmc

from ecodev_front.constants import INDEX, LABEL, TYPE, VALUE
from ecodev_front.ids import RADIO_GROUP
from ecodev_front.text import label_text


def radio_group(id: str,
                data: list[dict],
                value: str | None = None,
                label: str = '',
                size: str = 'sm',
                label_kwargs: dict = {},
                **kwargs
                ) -> dmc.RadioGroup:
    """
    Renders a radio group select component.

    data items must follow the {VALUE: ..., LABEL: ...} format.
    """
    radios = dmc.Group(
        [dmc.Radio(item[LABEL], value=item[VALUE], size=size) for item in data],
        gap='sm',
    )
    group = dmc.RadioGroup(
        id={TYPE: RADIO_GROUP, INDEX: id},
        value=value if value is not None else data[0][VALUE],
        persistence=True,
        persistence_type='session',
        children=radios,
        **kwargs
    )
    if not label:
        return group

    return dmc.Stack([label_text(label, **label_kwargs), group], gap='0px')
