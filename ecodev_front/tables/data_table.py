"""
Module implementing a generic Dash AG Grid table
"""
from typing import Any
from typing import Dict
from typing import List
from typing import Union

import dash_ag_grid as dag
from ecodev_core import logger_get
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict

log = logger_get(__name__)
locale_fr_FR = """d3.formatLocale({
  "decimal": ",",
  "thousands": "\u00a0",
  "grouping": [3],
  "currency": ["", "\u00a0€"],
  "percent": "\u202f%",
  "nan": ""
})"""


class DashAgGridEnterprise(BaseSettings):
    """
    Simple authentication configuration class
    """
    dag_license_key: str = ''
    enable_dag_enterprise: bool = True
    model_config = SettingsConfigDict(env_file='.env')


DAG_ENTERPRISE_AUTH = DashAgGridEnterprise()


def data_table(id: str | dict,
               row_data: list[dict[Any, Any]] | Any,
               column_defs: list[dict[Any, Any]] | None = None,
               default_col_def: dict | None = None,

               style: dict | None = None,
               row_style: dict | None = None,
               dash_grid_options: dict | None = None,

               pagination: bool = False,
               pagination_page_size: int = 5,

               tree_table: bool = False,

               floating_filter: bool = False,
               wrap_text: bool = False,
               theme: str = 'ag-theme-quartz',
               side_filter: bool = False,
               autogenerate_column_defs: bool = True,
               selected_rows: list[dict[Any, Any]] | Any = None,
               auto_height: bool = False,

               hide_empty_cols: bool = False,
               empty_cols_to_show: list[str] = [],

               get_row_id: str | None = None,

               draggable: bool = False,

               row_selection: str = 'single',
               suppress_row_click_selection: bool = True,
               group_selects_children: bool = True,

               header_name: str = '',
               default_expanded_depth: int = 0,
               auto_group_column_field: str | None = None,


               **kwargs,
               ) -> dag.AgGrid:
    """
    Generic Dash AG Grid table

    Args:
        id (str | dict): id of the table.
        row_data (list[dict[Any, Any]] | Any): list of rows to display in the table.
        column_defs (list[dict[Any, Any]]): list of column definitions.
        default_col_def (dict): default column definition.
        style (dict): style of the table.
        row_style (dict): style of the rows.
        dash_grid_options (dict): dash grid options.

        pagination (bool): if True, adds pagination to the table.
        pagination_page_size (int): length of the pagination.

        tree_table (bool): if True, the table is a tree table.
        header_name (str): name of the header of the tree table.
            default_expanded_depth (int): default expanded depth of the tree table. Defaults to 0.
            (0 = All collapsed, 1 = First level expanded, -1 = All expanded)
        auto_group_column_field (str): field whose values will be used in the autogroup column.
            If None, then then values of `path` will be used. Defaults to None.

        side_filter (bool): if True, adds a side bar with filtering options. Filters \
            will be generated for columns according to the config in column_defs. Overwrites
            the sidebar key in dash_grid_options
        autogenerate_column_defs (bool): if True, creates column_defs from row_data if \
            column_defs is not provided. Defaults to True.

        auto_height (list): if True, the grid to auto-sizes its height to the number of rows \
            displayed inside the grid. Overwrites the domLayout key in dash_grid_options and
            height in style
        group_selects_children (bool): if True, then selecting a node will select all its \
            children. Defaults to True.

        get_row_id (Optional[str]): js function to assign the `RowID` of each row in row_data \
            from the table's data. Ex : "params.data.id" to assign it to "id" field.
            See https://dash.plotly.com/dash-ag-grid/row-ids for more information.
        selected_rows (list): list of rows to select. Applies only to table with selectable \
            columns. selected_rows must be initialized to an empty list if no rows are selected.
        row_selection (str): selection mode of the table. Defaults to 'single'.
            Possible values are 'single', 'multiple' and 'singleRow'.
        suppress_row_click_selection (bool): Prevents selecting a row by clicking anywhere on it.
        Selection only happens via the checkbox. This avoids accidental selection when users click
        to expand/collapse.

        theme (str): theme of the table. Defaults to 'ag-theme-quartz'.
    """

    column_defs = column_defs or _create_default_column_definitions(
        row_data) if autogenerate_column_defs else []

    style = style
    default_col_def = default_col_def or {
        # enable floating filters by default
        'floatingFilter': floating_filter,
        'filter': 'agTextColumnFilter',
        # 'wrapHeaderText': True,
        # make row overflow
        'wrapText': wrap_text,
    }
    row_style = row_style

    dash_grid_options = dash_grid_options or {
        'colResizeDefault': 'shift',
        'rowSelection': row_selection,
        'suppressRowClickSelection': suppress_row_click_selection,
        'headerHeight': 50,
        'groupHeaderHeight': 30,
        # Enables pagination
        'pagination': pagination,
        'paginationPageSize': pagination_page_size,
        'groupSelectsChildren': group_selects_children,
    }

    if side_filter:
        dash_grid_options['sideBar'] = 'filters'

    if tree_table:
        dash_grid_options |= {
            'autoGroupColumnDef': {
                'field': auto_group_column_field,
                'headerName': header_name,
                'filterParams': {'treeList': True},
                'cellRendererParams': {
                    'suppressCount': True,
                },
            },
            'getDataPath': {'function': 'getDataPath(params)'},
            'treeData': True,
            'groupDefaultExpanded': default_expanded_depth,
        }

    if auto_height:
        dash_grid_options['domLayout'] = 'autoHeight'
        if isinstance(style, dict):
            style['height'] = None
        else:
            style = {'height': None}

    row_data = row_data if isinstance(row_data, list) else row_data.to_dict('records')

    if hide_empty_cols:
        empty_cols_idx = []
        for idx, col_def in enumerate(column_defs):
            if (col := col_def['field']) not in empty_cols_to_show:
                for row in row_data:
                    if value := row.get(col, None):
                        break
                if value is None:
                    empty_cols_idx.append(idx)

        column_defs = [col_def for idx, col_def in enumerate(column_defs)
                       if idx not in empty_cols_idx]

    if draggable:
        dash_grid_options |= {
            'rowDragManaged': True,
            'animateRows': True,
            'domLayout': 'autoHeight',
            'autoHeight': True,
            'rowDragEntireRow': True,
            'rowDragMultiRow': 'single',
            'suppressMaintainUnsortedOrder': True,
            'rowSelection': 'single',
        }

    return dag.AgGrid(
        id=id,
        enableEnterpriseModules=True,
        licenseKey='',
        columnDefs=column_defs,
        rowData=row_data,
        defaultColDef=default_col_def,
        style=style,
        getRowStyle=row_style,
        columnSize='responsiveSizeToFit',
        dashGridOptions=dash_grid_options,
        className=theme,

        getRowId=get_row_id,
        selectedRows=selected_rows or [],

        **kwargs,
    )


def _create_default_column_definitions(data: Union[List[Dict], Any]) -> List[Dict[str, str]]:
    """
    Iterates over the list of column definitions and creates default definitions
    """
    if isinstance(data, list):
        return [{'field': col, 'headerName': col.replace('_', ' ').title()}
                for col in data[0].keys()]

    return [{'field': col, 'headerName': col.replace('_', ' ').title()} for col in data.columns]
