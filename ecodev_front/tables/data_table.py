"""
Module implementing a generic Dash AG Grid table
"""
from typing import Any
from typing import Dict
from typing import List
from typing import Union

import dash_ag_grid as dag
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict

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
               theme: str = 'ag-theme-quartz'
               ) -> dag.AgGrid:
    """
    Generic Dash AG Grid table
    """

    column_defs = column_defs or _create_default_column_definitions(row_data)
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

    if tree_table:
        dash_grid_options |= {'autoGroupColumnDef': {
            'cellRendererParams': {
                'suppressCount': True,
            },
            'getDataPath': {'function': 'getDataPath(params)'},
            'treeData': True,
            'rowSelection': 'single'
        }}

    return dag.AgGrid(
        id=id,
        enableEnterpriseModules=True,
        licenseKey='',
        columnDefs=column_defs,
        rowData=row_data if isinstance(row_data, list) else row_data.to_dict('records'),
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
