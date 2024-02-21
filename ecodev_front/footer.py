"""
BLA
"""
from typing import Dict
from typing import Union


def footer_style(
    color: str = '#0066A1', height: str = '5vh', display: str = 'flex'
) -> Dict[str, Union[str, int]]:
    """
    Main app footer style
    """
    return {
        'position': 'fixed',
        'bottom': 0,
        'height': height,
        'width': '100vw',
        'paddingBottom': '10px',
        'backgroundColor': color,
        'color': 'white',
        'display': display,
        'textAlign': 'center',
        'alignContent': 'center',
        'justifyContent': 'center',
    }
