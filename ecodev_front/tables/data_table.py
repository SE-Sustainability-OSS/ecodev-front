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
               row_data: List[Dict] | Any,
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
               selected_rows: List[Dict] | Any = None,
               auto_height: bool = False,
               hide_empty_cols: bool = False,
               empty_cols_to_show: list[str] = []
               ) -> dag.AgGrid:
    """
    Generic Dash AG Grid table

    Args:
        side_filter (bool) : if True, adds a side bar with filtering options. Filters \
            will be generated for columns according to the config in column_defs. Overwrites
            the sidebar key in dash_grid_options
        autogenerate_column_defs (bool) : if True, creates column_defs from row_data if \
            column_defs is not provided. Defaults to True.
        selected_rows (list) : list of rows to select. Applies only to table with selectable \
            columns
        auto_height (list) : if True, the grid to auto-sizes its height to the number of rows \
            displayed inside the grid. Overwrites the domLayout key in dash_grid_options and
            height in style
    """

    column_defs = column_defs or _create_default_column_definitions(
        row_data) if autogenerate_column_defs else []
    style = style
    default_col_def = default_col_def or {
        # enable floating filters by default
        'floatingFilter': floating_filter,
        # 'wrapHeaderText': True,
        # make row overflow
        'wrapText': wrap_text,
    }
    row_style = row_style

    dash_grid_options = dash_grid_options or {
        'colResizeDefault': 'shift',
        'rowSelection': 'single',
        'headerHeight': 50,
        'groupHeaderHeight': 30,
        # Enables pagination
        'pagination': pagination,
        'paginationPageSize': pagination_page_size,
    }

    if side_filter:
        dash_grid_options['sideBar'] = 'filters'

    if tree_table:
        dash_grid_options |= {'autoGroupColumnDef': {
            'cellRendererParams': {
                'suppressCount': True,
            },
            'getDataPath': {'function': 'getDataPath(params)'},
            'treeData': True,
            'rowSelection': 'single'
        }}

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

    return dag.AgGrid(
        id=id,
        enableEnterpriseModules=True,
        licenseKey='',
        columnDefs=column_defs,
        rowData=row_data,
        selectedRows=selected_rows,
        defaultColDef=default_col_def,
        style=style,
        getRowStyle=row_style,
        columnSize='responsiveSizeToFit',
        dashGridOptions=dash_grid_options,
        className=theme
    )


def _create_default_column_definitions(data: Union[List[Dict], Any]) -> List[Dict[str, str]]:
    """
    Iterates over the list of column definitions and creates default definitions
    """
    if isinstance(data, list):
        return [{'field': col, 'headerName': col.replace('_', ' ').title()}
                for col in data[0].keys()]

    return [{'field': col, 'headerName': col.replace('_', ' ').title()} for col in data.columns]
