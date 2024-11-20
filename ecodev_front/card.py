"""
Components to create standardised card across apps.
"""
from typing import Any
from typing import Optional

import dash_mantine_components as dmc
from dash import html
from dash_iconify import DashIconify


DEFAULT_STYLE = {
    'position': 'flex',
    'justifyContent': 'center'}


def background_card(children: list[dmc.CardSection | html.Div],
                    style: dict[str, str | int | float] | None = None,
                    className: str = '',
                    card_id: str = ''
                    ) -> dmc.Card:
    """
    Returns a formatted dmc.Card
    """
    return dmc.Card(children, radius='md', shadow='sm', style=style or DEFAULT_STYLE,
                    className=className, id=card_id)


def card_title(title: str,
               size: int = 16,
               title_id: str = '',
               color: str = 'white',
               font: str = 'Averta',
               align: str = 'left',
               background_color: str = '#0066a1',
               component: Optional[Any] = None,
               justify: str = 'space-between'
               ) -> dmc.CardSection:
    """
    Returns dmc.CardSection with a standardised dmc.Text and possible selection options and an
    optional additional component (e.g. select, slider, etc.) on its right hand side.
    """
    content = [dmc.Text(title, fz=size, fw=900, c=color, ff=font, ta=align, id=title_id,
                        bg=background_color, p=10)]

    content += component if isinstance(component, list) else [component]
    return card_section(
        dmc.Group(children=content,
                  style={'backgroundColor': background_color, 'padding-right': '10px'},
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
               color: str = '#A0AEC0',
               size: int = 32,
               text_id: str = ''
               ) -> dmc.Text:
    """
    Returns a formatted dmc.Text element from a string
    """
    return dmc.Text(text, c=color, fz=size, fw=700, id=text_id)


def kpi(icon: DashIconify,
        value: int | float | str,
        unit: Optional[str] = None,
        title: str | None = None,
        tooltip: str | None = None,
        c: str = '#0066a1',
        fz: int = 24,
        fw: int = 700) -> dmc.Tooltip:
    """
    Render a KPI card
    """
    return dmc.Tooltip([
        dmc.Card([dmc.Stack([
            dmc.Text(title, c='gray', fz=(fz - 6), fw=fw),
            dmc.Group(
                [
                    icon,
                    dmc.Text(value, c=c, fz=fz, fw=1000),
                    dmc.Text(unit, c='gray', fz=(fz - 8), fw=1000),
                ], gap='xs'
            ),
        ], bg='#f7f8f9', w=250)])
    ],  label=tooltip, position='top', offset=3,
        withArrow=True, closeDelay=300, color=c)
