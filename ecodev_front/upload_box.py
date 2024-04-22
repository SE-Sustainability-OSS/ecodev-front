"""
Component which allows document upload.
"""
from typing import Dict
from typing import Union

from dash import dcc
from dash import html

DEFAULT_STYLE = {'height': '30vh',
                 'lineHeight': '60px',
                 'borderWidth': '1px',
                 'borderStyle': 'dashed',
                 'borderRadius': '10px',
                 'textAlign': 'center',
                 'margin': 'auto',
                 'color': '#A0AEC0',
                 'verticalAlign': 'middle'}


def upload_box(id: str,
               label: str,
               multiple: bool,
               style: Union[Dict[str, str], None] = None
               ) -> dcc.Upload:
    """
    Returns an upload box
    """
    return dcc.Upload(id=id, multiple=multiple, style=style or DEFAULT_STYLE,
                      children=html.H5(label, style={'display': 'flex',
                                                     'justifyContent': 'center',
                                                     'alignItems': 'center',
                                                     'textAlign': 'center'}))
