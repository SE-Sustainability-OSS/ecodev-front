from dash_iconify import DashIconify


def dash_icon(icon: str,
              width: int | None = None,
              height: int | None = None,
              color: str = 'default-color') -> DashIconify:
    """
    Renders a DashIconify icon
    """
    return DashIconify(icon=icon, width=width, height=height, color=color)
