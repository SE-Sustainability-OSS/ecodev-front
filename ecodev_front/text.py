"""
File containing formatted text components
"""
import dash_mantine_components as dmc


def text_header(text: str) -> dmc.Text:
    """
    Renders a stylized dmc.Text component to display headers
    """
    return dmc.Text(children=text, size='xl', fw=700, ta='center')


def sub_text(text: str) -> dmc.Text:
    """
    Renders a stylized dmc.Text component to display sub-texts
    """
    return dmc.Text(children=text, ta='center')
