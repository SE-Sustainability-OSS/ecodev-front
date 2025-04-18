from ecodev_front.page import Page

from dash import register_page


def add_page(page: Page) -> None:
    """
    Registers the page with Dash, and pass through a custom page layout to instantiate a Dash page.
    """
    register_page(
        module=page.module,
        path=page.url,
        title=page.title,
        layout=page.render_layout
    )