from typing import Dict

import dash_mantine_components as dmc
import pandas as pd

from dash import callback
from dash import dcc
from dash import Input
from dash import Output
from dash import State
from dash_iconify import DashIconify

BTN_SUFFIX = '-btn'
DATA_SUFFIX = '-data'

def graph_and_download(
    id_graph: str,
    style: Dict = None
) -> dmc.Stack:
    """
    component with a graph and a download button, the download btn
    aims at downloading the data associated to the graph
    """
    return dmc.Stack(
        children=[
            dcc.Graph(id=id_graph, style={'width': '100%', 'height': '100%'}),
            dmc.Button(
                children=[
                    dmc.Tooltip(
                        children=DashIconify(icon='material-symbols:download'),
                        label='Download the data associated to the graph',
                        position='left',
                    ),
                ],
                id=id_graph+BTN_SUFFIX,
                c='primary',
                className='me-1',
                disabled=False,
                style={
                    'font-size': '20px',
                    'z-index': '1',
                    'left': '85%',
                    'bottom': '50px',
                }
            ),
            dcc.Download(id=id_graph+DATA_SUFFIX),
        ],
        style=style,
    )


def create_dwld_callback(id: str) -> callback:
    """
    Define the callback for the graph and the download button
    """
    def dwld_callback(n_clicks, data):
        if n_clicks:
            df = pd.DataFrame(data)
            return dcc.send_data_frame(df.to_excel, f'{id}.xlsx')

    callback(
        Output(id+DATA_SUFFIX, 'data'),
        Input(id+BTN_SUFFIX, 'n_clicks'),
        State(id+BTN_SUFFIX, 'data'),
        prevent_initial_call=True,
    )(dwld_callback)