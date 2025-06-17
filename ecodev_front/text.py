"""
File containing formatted text components
"""
import dash_mantine_components as dmc


def app_title(text: str, c: str = 'black', ta: str = 'left', mb: int = 10, **kwargs) -> dmc.Title:
    """
    Renders a formatted text for app main page headers
    """
    return dmc.Title(text, order=1, ta=ta, c=c, tt='capitalize', mb=mb, **kwargs)


def page_title(text: str, c: str = '#0066a1', ta: str = 'left', **kwargs) -> dmc.Title:
    """
    Renders a formatted title text for page headers
    """
    return dmc.Title(text, order=2, ta=ta, c=c, tt='capitalize', ff='Averta Bold', **kwargs)


def section_title(text: str, c: str = '#424242', ta: str = 'left', **kwargs) -> dmc.Title:
    """
    Renders a formatted text for page sections
    """
    return dmc.Title(text, order=3, c=c, ta=ta, tt='capitalize', ff='Averta Bold', **kwargs)


def subtitle(text: str, c: str = 'dimmed', ta: str = 'left', **kwargs) -> dmc.Title:
    """
    Renders a formatted header subtitle
    """
    return dmc.Text(text, fz=16, ta=ta, c=c, fs='italic', **kwargs)


def text_title(text: str, c: str = '#0066a1', ta: str = 'left', **kwargs) -> dmc.Text:
    """
    Renders a stylized dmc.Text component to display body text headers
    """
    return dmc.Title(children=text, order=4, ff='Averta Bold', c=c, ta=ta, **kwargs)


def subtext(text: str, c: str = '#989898', ta: str = 'left', **kwargs) -> dmc.Text:
    """
    Renders a stylized dmc.Text component to display body sub-texts
    """
    return dmc.Text(children=text, c=c, fz=14, fs='italic', ta=ta, **kwargs)


def label_text(text: str, ta='left') -> dmc.Text:
    """
    Renders a component label, aligned with dmc component labels.
    To be used on custom made components
    """
    return dmc.Text(text, fz='0.875rem', fs='normal', ff='Cabin, sans-serif', ta=ta)
