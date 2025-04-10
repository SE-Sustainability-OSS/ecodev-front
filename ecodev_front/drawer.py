import dash_mantine_components as dmc


def drawer(title: str,
           id: str = '',
           padding: str | int = 'md',
           size: str = '60%'):
    """
    Renders a dmc.Drawer
    """
    return dmc.Drawer(
        title=title,
        id=id,
        padding=padding,
        size=size
    )
