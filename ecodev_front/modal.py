"""
Component which to display a dmc.Modal on the side of the screen
"""
import dash_mantine_components as dmc


def modal(id: str,
          size: int | str = '80%',
          ) -> dmc.Modal:
    """
    Returns a dmc.Modal which can be used to display content on the screen temporarily
    """
    return dmc.Modal(id=id, size=size)
