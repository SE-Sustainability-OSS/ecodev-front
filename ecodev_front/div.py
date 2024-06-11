from dash import html


def render_formatted_div(div_id: str) -> html.Div:
    """
    Renders a formatted html.Div with content at the center
    Useful to center plotly graphs
    """
    return html.Div(id=div_id, style={'height': '100%', 'width': '100%'})
