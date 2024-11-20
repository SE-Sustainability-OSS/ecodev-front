"""
Module implementing helper methods to create custom column definitions for Dash AG Grid tables
"""
from enum import Enum
from enum import unique
from typing import Any
from typing import Dict
from typing import Optional

from ecodev_front.tables.data_table import locale_fr_FR


@unique
class DagColTypes(str, Enum):
    """
    Enum listing the different filter types for a Dash AG Grid table
    """
    NUMERICAL = 'numerical'
    DATE = 'date'


DAG_FILTERS = {
    DagColTypes.NUMERICAL: 'agNumberColumnFilter',
    DagColTypes.DATE: 'agDateColumnFilter'
}

DAG_TYPES = {
    DagColTypes.NUMERICAL: 'numberColumn',
    DagColTypes.DATE: 'dateString'
}


def custom_column_def(field: str,
                      header_name: Optional[str] = None,
                      width: Optional[int] = None,
                      dag_type: Optional[DagColTypes] = None,
                      sortable: Optional[bool] = False,
                      editable: bool | Dict = False,
                      value_formatter: Optional[str] = None,
                      locale: str = locale_fr_FR,
                      value_getter: Optional[str] = None,
                      cell_data_style: Optional[str] = None,
                      cell_renderer: Optional[str] = None,
                      cell_renderer_params: Optional[Dict] = None,
                      cell_style: Optional[Dict] = None,
                      cell_editor: Optional[str] = None,
                      cell_editor_params: Optional[Dict] = None,
                      other_params: Optional[dict] = {}) -> Dict[str, Any]:
    """
    Creates a custom def dict
    """
    return {
        'field': field,
        'headerName': header_name or field.replace('_', ' ').title(),
        'width': width,
        'filter': DAG_FILTERS.get(dag_type, True),  # type: ignore[arg-type]
        'sortable': sortable,
        'editable': editable,
        'type': DAG_TYPES.get(dag_type),  # type: ignore[arg-type]
        'valueFormatter': _get_value_formatter(dag_type, value_formatter, locale),
        'valueGetter': {'function': value_getter},
        'filterValueGetter': {'function': "d3.timeParse('%d/%m/%Y')(params.data.date)"} if
        dag_type == DagColTypes.DATE else None,
        'cellDataStyle': cell_data_style,
        'cellRenderer': cell_renderer,
        'cellRendererParams': cell_renderer_params,
        'tooltipField': field,
        'cellStyle': cell_style,
        'cellEditor': cell_editor,
        'cellEditorParams': cell_editor_params
    } | other_params


def _get_value_formatter(dag_type: DagColTypes | None,
                         value_formatter: str | None,
                         locale: str
                         ) -> Optional[Dict[str, str]]:
    """
    Returns a value formatter based on the type of the column
    """
    if dag_type == DagColTypes.NUMERICAL:
        return {'function': f"{locale}.format(',.{value_formatter}')(params.value)"}
    return {'function': 'params.data.date'} if dag_type == DagColTypes.DATE else None
