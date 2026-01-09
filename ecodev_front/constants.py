"""
Callbacks constants
"""
CHILDREN = 'children'
DATA = 'data'
PATHNAME = 'pathname'
N_CLICKS = 'n_clicks'
VALUE = 'value'
DISABLED = 'disabled'
STYLE = 'style'
ACTIVE = 'active'
LOCAL = 'local'
OPENED = 'opened'
CONTENTS = 'contents'
FILENAME = 'filename'
TYPE = 'type'
INDEX = 'index'
ID = 'id'
VISIBLE = 'visible'
CHECKED = 'checked'
HIDDEN = 'hidden'
HREF = 'href'
FIGURE = 'figure'

CLICK_DATA = 'clickData'
ERROR = 'error'
LOADING = 'loading'
ALLOW_STEP_CLICK = 'allowStepClick'
STEPS = 'steps'
LABEL = 'label'
OPTIONS = 'options'
REQUIRED = 'required'
DISPLAY = 'display'
SEND_NOTIFICATIONS = 'sendNotifications'
TITLE = 'title'
ACTION = 'action'
MESSAGE = 'message'
ICON = 'icon'
COLOR = 'color'
CREATED_AT = 'created_at'
WITH_CLOSE_BUTTON = 'withCloseButton'
N_INTERVALS = 'n_intervals'

VARIANT = 'variant'

"""
Table constants
"""
CELL_RENDERER_DATA = 'cellRendererData'
ROW_DATA = 'rowData'
ROW_INDEX = 'rowIndex'
CELL_CLICKED = 'cellClicked'
CELL_VALUE_CHANGED = 'cellValueChanged'
ROW_ID = 'rowId'
COL_ID = 'colId'
SELECTED_ROWS = 'selectedRows'
ROW_TRANSACTION = 'rowTransaction'

"""
Stores
"""
SESSION_STORE = 'session'
LOCAL_STORE = 'local'
NOTIFICATION_ID = 'notification-id'

"""
URLS
"""
MAIN_PAGE_URL = '/'
LOGIN_PAGE_URL = '/login'

"""
Unit Converters
"""
THOUSAND = 1000
MILLION = 1_000_000
BILLION = 1_000_000_000
TRILLION = 1_000_000_000_000

"""
DATA VERSIONING
"""
UPDATE_TYPE = 'update_type'
INSERTED = 'inserted'
UPDATED = 'updated'
DELETED = 'deleted'
UNCHANGED = 'unchanged'
OLD_VALUE = 'old-value'
NEW_VALUE = 'new-value'
MAIN_ID = 'main-id'
STAGING_ID = 'staging-id'
UPDATED_AT = 'updated_at'


__all__ = [
    'CHILDREN',
    'DATA',
    'PATHNAME',
    'N_CLICKS',
    'VALUE',
    'DISABLED',
    'STYLE',
    'ACTIVE',
    'LOCAL',
    'OPENED',
    'CONTENTS',
    'FILENAME',
    'TYPE',
    'INDEX',
    'ID',
    'VISIBLE',
    'CHECKED',
    'HIDDEN',
    'HREF',
    'FIGURE',

    'CLICK_DATA',
    'ERROR',
    'LOADING',
    'ALLOW_STEP_CLICK',
    'STEPS',
    'LABEL',
    'OPTIONS',
    'REQUIRED',
    'DISPLAY',
    'SEND_NOTIFICATIONS',
    'TITLE',
    'ACTION',
    'MESSAGE',
    'ICON',
    'COLOR',
    'CREATED_AT',
    'WITH_CLOSE_BUTTON',
    'N_INTERVALS',

    'CELL_RENDERER_DATA',
    'ROW_DATA',
    'ROW_INDEX',
    'CELL_CLICKED',
    'CELL_VALUE_CHANGED',
    'ROW_ID',
    'COL_ID',

    'SESSION_STORE',
    'LOCAL_STORE',
    'NOTIFICATION_ID',

    'MAIN_PAGE_URL',
    'LOGIN_PAGE_URL',

    'THOUSAND',
    'MILLION',
    'BILLION',
    'TRILLION',

    'UPDATE_TYPE',
    'INSERTED',
    'UPDATED',
    'DELETED',
    'UNCHANGED',
    'OLD_VALUE',
    'NEW_VALUE',
    'MAIN_ID',
    'STAGING_ID',
    'UPDATED_AT',

    'VARIANT',
    'ROW_TRANSACTION'
]
