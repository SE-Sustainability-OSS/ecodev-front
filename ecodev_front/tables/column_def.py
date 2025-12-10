"""
Module implementing helper methods to create custom column definitions for Dash AG Grid tables
"""
from enum import Enum
from enum import unique
from typing import Any
from typing import Dict
from typing import Optional

from ecodev_front.constants import COL_ID
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


def custom_column_def(field: str | None = None,
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
                      single_click_edit: Optional[bool] = False,
                      pinned: Optional[str] = None,
                      checkbox_selection: Optional[bool] = False,
                      header_checkbox_selection: Optional[bool] = False,
                      suppress_movable: Optional[bool] = False,
                      suppress_menu: Optional[bool] = False,
                      header_tooltip: Optional[str] = None,
                      max_width: Optional[int] = None,
                      col_id: Optional[str] = None,
                      filter: Optional[bool] = None,
                      floating_filter: Optional[bool] = None,
                      other_params: Optional[dict] = {}) -> Dict[str, Any]:
    """
    Creates a column definition dictionary for Dash AG Grid.

    Column definitions configure the behavior and appearance of individual columns
    in the grid. See https://dash.plotly.com/dash-ag-grid/column-definitions

    Args:
        field (str): The field name that maps to a key in the row data. This is the
            primary identifier linking the column to the data source.
        header_name (Optional[str]): The display name shown in the column header.
            Defaults to a title-cased version of `field` with underscores replaced by spaces.
        header_tooltip (Optional[str]): The tooltip shown in the column header.
            Defaults to None.
        width (Optional[int]): The initial width of the column in pixels.
            See https://dash.plotly.com/dash-ag-grid/column-sizing
        max_width (Optional[int]): The maximum width of the column in pixels. Use max-width when
            the default column size = 'responsiveSizeToFit'
        col_id (Optional[str]): The ID of the column.
            See https://dash.plotly.com/dash-ag-grid/column-ids
        filter (Optional[bool]): If True, enables filtering when clicking the column header.
            Defaults to True.
        floating_filter (Optional[bool]): If True, enables the floating filter feature of the column
            Defaults to True.
        dag_type (Optional[DagColTypes]): The column data type (NUMERICAL or DATE).
            Determines the appropriate filter type and value formatter.
        sortable (Optional[bool]): If True, enables sorting when clicking the column header.
            Defaults to False.
        editable (bool | Dict): If True, allows cell editing. Can also be a dict with
            a 'function' key for conditional editing based on row data.
            See https://dash.plotly.com/dash-ag-grid/cell-editing
        value_formatter (Optional[str]): A d3-format string or JS function to format
            displayed cell values. For NUMERICAL type, specifies decimal precision.
            See https://dash.plotly.com/dash-ag-grid/value-formatters
        locale (str): The d3.formatLocale configuration for number/currency formatting.
            Defaults to French locale (comma decimal, space thousands separator).
        value_getter (Optional[str]): A JS function string to compute cell values from
            row data, useful for calculated or derived columns.
            See https://dash.plotly.com/dash-ag-grid/value-getters
        cell_data_style (Optional[str]): Custom data style attribute for cells.
        cell_renderer (Optional[str]): Name of a custom component to render cell content.
            Use for buttons, links, or complex cell displays.
            See https://dash.plotly.com/dash-ag-grid/cell-renderer-components
        cell_renderer_params (Optional[Dict]): Parameters passed to the cellRenderer component.
        cell_style (Optional[Dict]): CSS style dict applied to cells in this column.
            See https://dash.plotly.com/dash-ag-grid/cell-styling
        cell_editor (Optional[str]): Name of a custom editor component for cell editing.
            See https://dash.plotly.com/dash-ag-grid/cell-editor-components
        cell_editor_params (Optional[Dict]): Parameters passed to the cellEditor component.
        single_click_edit (Optional[bool]): If True, enables single click edit when clicking the
            column cell. Defaults to False.
        other_params (Optional[dict]): Additional AG Grid column properties to merge
            into the definition.
        pinned (Optional[str]): Position of the column. Defaults to None.
            Possible values are 'left', 'right', 'center'.
        checkbox_selection (Optional[bool]): If True, enables checkbox selection when clicking the
            column cell. Defaults to False.
        header_checkbox_selection (Optional[bool]): If True, enables checkbox selection when
            clicking the header. Defaults to False.
        suppress_movable (Optional[bool]): If True, disables the movable feature of the column.
        suppress_menu (Optional[bool]): If True, disables the menu feature of the column.

    Returns:
        Dict[str, Any]: A column definition dictionary compatible with Dash AG Grid's columnDefs.
    """
    return {
        'field': field,
        'headerName': header_name or field.replace('_', ' ').title() if field else '',
        'headerTooltip': header_tooltip,
        'width': width,
        'maxWidth': max_width,
        COL_ID: col_id,
        'filter': filter or DAG_FILTERS.get(dag_type, True),  # type: ignore[arg-type]
        'floatingFilter': floating_filter,
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
        'cellEditorParams': cell_editor_params,
        'singleClickEdit': single_click_edit,
        'pinned': pinned,
        'checkboxSelection': checkbox_selection,
        'headerCheckboxSelection': header_checkbox_selection,
        'suppressMovable': suppress_movable,
        'suppressMenu': suppress_menu,
    } | (other_params or {})


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


CELL_STYLE_CENTER = {
    'display': 'flex',
    'justifyContent': 'center',
    'alignItems': 'center',
}

CHECKBOX_COLUMN_DEF = custom_column_def(
    max_width=50,
    pinned='left',
    checkbox_selection=True,
    header_checkbox_selection=True,
    suppress_movable=True,
    suppress_menu=True,
)
