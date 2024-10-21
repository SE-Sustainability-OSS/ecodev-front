import dash_mantine_components as dmc


def container(id: str,
              style: dict[str, str] | None = None):
    """
    Function to render a container (base layout of a page)
    """
    return dmc.Container(id=id, fluid=True, style=style or {})
