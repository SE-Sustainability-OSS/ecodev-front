"""
File containing formatted text components
"""
import dash_mantine_components as dmc



def app_name_header(text: str, c: str = 'black', ta: str='left') -> dmc.Title:
    """
    Renders a formatted text for app main page headers
    """
    return dmc.Title(text, order=1, ta=ta, c=c, tt='capitalize')



def page_header(text: str, c: str = '#0066a1', ta: str='left') -> dmc.Title:
    """
    Renders a formatted text for page headers
    """
    return dmc.Title(text, order=2, ta=ta, c=c, tt='capitalize')


def section_header(text: str, c: str ='#424242', ta: str = 'left') -> dmc.Title:
    """
    Renders a formatted text for page sections
    """
    return dmc.Title(text, order=3, c=c, ta=ta, tt='capitalize')


def header_subtitle(text: str, c: str = 'dimmed', ta: str='left') -> dmc.Title:
    """
    Renders a formatted header subtitle
    """
    return dmc.Text(text, fz=16, ta=ta, c=c, fs='italic', truncate="end")


def text_header(text: str, c: str ='#0066a1', ta: str = 'left') -> dmc.Text:
    """
    Renders a stylized dmc.Text component to display body text headers
    """
    return dmc.Title(children=text, order=4, fw=900, c=c, ta=ta)


def sub_text(text: str, c: str = 'dimmed', ta: str='left') -> dmc.Text:
    """
    Renders a stylized dmc.Text component to display body sub-texts
    """
    return dmc.Text(children=text, c=c, fz=15, fs='italic', ta=ta)
