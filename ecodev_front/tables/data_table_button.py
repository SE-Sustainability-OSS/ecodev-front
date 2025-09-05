
from typing import Any


def dash_ag_grid_button(field: str,
                         value=None,
                         color='green',
                         variant='filled',
                         margin='1px',
                         header_name='',
                         cell_renderer='DMC_Button',
                         radius='md',
                         left_icon=None,
                         right_icon=None,
                         **kwargs
                         ) -> dict[str, Any]:
    """
    Helper function to display a dmc.Button in Dash AG Grid column
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
            'value': value,
            'leftIcon': left_icon,
            'rightIcon': right_icon
        },
        **kwargs
    }
    
