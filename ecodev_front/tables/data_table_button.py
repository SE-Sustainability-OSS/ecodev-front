
from typing import Any


def dash_ag_grid_button(field: str,
                         value:str =None,
                         header_name: str = '',
                         color:str = 'green',
                         variant:str = 'filled',
                         margin:str = '1px',
                         cell_renderer:str = 'DMC_Button',
                         radius:str = 'md',
                         left_icon:str = None,
                         width: int = None
                         ) -> dict[str, Any]:
    """
    Create a configuration dictionary for a Dash AG Grid column
    that renders a DMC Button.

    This helper function simplifies adding a clickable button
    in an AG Grid column by returning the column definition
    with all necessary parameters.

    Args:
        field (str): The name of the column field in the data.
        value (str, optional): The text to display on the button.
            Defaults to the field name if not provided.
        color (str, optional): The color of the button. Defaults to 'green'.
        variant (str, optional): The button variant (e.g., 'filled', 'outline'). Defaults to 
            'filled'.
        margin (str, optional): CSS margin around the button. Defaults to '1px'.
        cell_renderer (str, optional): The name of the cell renderer component. Defaults to 
            'DMC_Button'.
        radius (str, optional): The border radius of the button. Defaults to 'md'.
        left_icon (str, optional): Icon to display on the left of the button text. Defaults to None.
        width (int, optional): Column width in pixels. Defaults to None.

    Returns:
        dict[str, Any]: A dictionary representing the column definition
        compatible with Dash AG Grid, including button styling and behavior.
    """
    return {
        'field': field,
        'headerName': header_name,
        'editable': False,
        'cellRenderer': cell_renderer,
        'cellRendererParams': {
            'color': color,
            'variant': variant,
            'radius': radius,
            'margin': margin,
            'value': value if value is not None else field,
            'leftIcon': left_icon,
        },
        'width': width
    }
    