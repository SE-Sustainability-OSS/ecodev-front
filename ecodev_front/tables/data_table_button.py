
from typing import Any


def dash_ag_grid_button(field: str,
                         color: str,
                         variant='filled',
                         margin='1px',
                         header_name=''
                         ) -> dict[str, Any]:
    """
    Helper function to display a dmc.Button in Dash AG Grid column
    """
    return {
        'field': field,
        'headerName': header_name,
        'editable': False,
        'cellRenderer': 'DMC_Button',
        'cellRendererParams': {
            'color': color,
            'variant': variant,
            'radius': 'md',
            'margin': margin,
            'value': field
        },
    }
