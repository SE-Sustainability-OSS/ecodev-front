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


def data_table(id: str,
               row_data: Union[List[Dict], Any],
               column_defs: list[dict[Any, Any]] | None = None,
               default_col_def: dict | None = None,
               auto_height: bool = True,
               style: dict | None = None,
               row_alternating_color='#f5f5f5',
               row_style: dict | None = None,
               dash_grid_options: dict | None = None,
               pagination: bool = False,
               pagination_page_size: int = 5
               ) -> dag.AgGrid:
    """
    Generic Dash AG Grid table
    """

    column_defs = column_defs or _create_default_column_definitions(row_data)
    style = style
    default_col_def = default_col_def or {
        # make every column use 'text' filter by default
        'filter': 'agTextColumnFilter',
        # enable floating filters by default
        'floatingFilter': True,
        # make columns resizable
        'resizable': True,
        'sortable': True,
        'wrapHeaderText': True,
        'autoHeaderHeight': True,
        'wrapText': True,
        # make row overflow
        'autoHeight': auto_height,
        # Make columns editable
        'editable': True
    }
    row_style = row_style or {
        'styleConditions': [
            {
                'condition': 'params.node.rowIndex % 2 === 1',
                'style': {'backgroundColor': row_alternating_color},
            },
        ]
    }

    dash_grid_options = dash_grid_options or {
        'colResizeDefault': 'shift',
        'rowSelection': 'single',
        'headerHeight': 30,
        'groupHeaderHeight': 30,
        # Enables pagination
        'pagination': pagination,
        'paginationPageSize': pagination_page_size,

    }

    return dag.AgGrid(
        id=id,
        enableEnterpriseModules=DAG_ENTERPRISE_AUTH.enable_dag_enterprise,
        licenseKey=DAG_ENTERPRISE_AUTH.dag_license_key,
        columnDefs=column_defs,
        rowData=row_data if isinstance(row_data, list) else row_data.to_dict('records'),
        defaultColDef=default_col_def,
        style=style,
        getRowStyle=row_style,
        columnSize='responsiveSizeToFit',
        dashGridOptions=dash_grid_options,
        className='ag-theme-material',
    )


def _create_default_column_definitions(data: Union[List[Dict], Any]) -> List[Dict[str, str]]:
    """
    Iterates over the list of column definitions and creates default definitions
    """
    if isinstance(data, list):
        return [{'field': col, 'headerName': col.replace('_', ' ').title()}
                for col in data[0].keys()]

    return [{'field': col, 'headerName': col.replace('_', ' ').title()} for col in data.columns]
