"""
Components to create standardised card across apps.
"""
from typing import Any
from typing import Optional

import dash_mantine_components as dmc

from . import theme_config
from ecodev_front.icon import dash_icon

DEFAULT_STYLE = {
    'position': 'flex',
    'justifyContent': 'center'}


def background_card(children: list,
                    style: dict[str, str | int | float] | None = None,
                    className: str = '',
                    card_id: str = '',
                    **kwargs
                    ) -> dmc.Card:
    """
    Returns a formatted dmc.Card
    """
    return dmc.Card(children, radius='md', shadow='sm', style=style or DEFAULT_STYLE,
                    className=className, id=card_id, **kwargs)


def card_title(title: str,
               size: int = 16,
               title_id: str = '',
               color: str = 'white',
               font: str = 'Averta',
               align: str = 'left',
               background_color: str | None = None,
               component: Optional[Any] = None,
               justify: str = 'space-between'
               ) -> dmc.CardSection:
    """
    Returns dmc.CardSection with a standardised dmc.Text and possible selection options and an
    optional additional component (e.g. select, slider, etc.) on its right hand side.
    """
    resolved_bg = background_color or theme_config.PRIMARY_COLOR
    content = [dmc.Text(title, fz=size, fw=900, c=color, ff=font, ta=align, id=title_id,
                        bg=resolved_bg, p=10, style={'flex': 1})]

    content += component if isinstance(component, list) else [component]
    return card_section(
        dmc.Group(children=content,
                  style={'backgroundColor': resolved_bg},
                  justify=justify
                  )
    )


def card_section(children: Any, graph: bool = False) -> dmc.CardSection:
    """
    Returns a formatted dmc.CardSection from passed dmc.Text
    """
    return dmc.CardSection(children,
                           withBorder=True,
                           style={'height': '100%', 'width': '100%'} if graph else {})


def macro_info(text: str | float,
               color: str | None = None,
               size: int = 32,
               text_id: str = ''
               ) -> dmc.Text:
    """
    Returns a formatted dmc.Text element from a string
    """
    return dmc.Text(text, c=color or theme_config.GRAY_COLOR, fz=size, fw=700, id=text_id)


def kpi(icon: str,
        value: int | float | str,
        unit: Optional[str] = None,
        title: str | None = None,
        tooltip: str | None = None,
        c: str | None = None,
        fz: int = 24,
        fw: int = 700) -> dmc.Tooltip:
    """
    Render a KPI card
    """
    resolved_c = c or theme_config.PRIMARY_COLOR
    return dmc.Tooltip([
        dmc.Card([dmc.Stack([
            dmc.Text(title, c='gray', fz=(fz - 6), fw=fw),
            dmc.Group(
                [
                    dash_icon(icon, width=30, color=resolved_c),
                    dmc.Text(value, c=resolved_c, fz=fz, fw=1000),
                    dmc.Text(unit, c='gray', fz=(fz - 8), fw=1000),
                ], gap='xs'
            ),
        ], bg='#f7f8f9', w=250)])
    ], label=tooltip, position='top', offset=3,
        withArrow=True, closeDelay=300, color=resolved_c)
