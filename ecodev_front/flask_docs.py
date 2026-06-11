"""
Flask routes and Dash callback wiring for JWT-protected MkDocs documentation.

Activate via enable_flask_docs(app); gated by dash_settings.with_docs flag.
"""
from pathlib import Path

from dash import callback
from dash import Input
from dash import no_update
from dash import Output
from ecodev_core import AUTH
from ecodev_core import safe_get_user
from ecodev_core import SETTINGS
from ecodev_core.settings import BASE_PATH
from flask import abort
from flask import redirect
from flask import send_from_directory
from flask import session as flask_session

from ecodev_front.constants import DATA
from ecodev_front.constants import DOCS_SESSION_KEY
from ecodev_front.constants import DOCS_URL
from ecodev_front.ids import DOCS_SYNC
from ecodev_front.ids import TOKEN

_REGISTERED_APPS: set[int] = set()


def with_docs() -> bool:
    """
    Returns True when Flask-served MkDocs documentation is enabled via config.
    """
    return getattr(SETTINGS.dash_settings, 'with_docs', False)


def _docs_target(path: str) -> str:
    """
    Resolves a URL path to the corresponding file within the built MkDocs site.
    """
    if not path:
        return 'index.html'
    if Path(path).suffix:
        return path
    return path.rstrip('/') + '/index.html'


def _is_valid_docs_jwt(raw_jwt: str) -> bool:
    """
    Returns True when raw_jwt decodes to a valid active user.
    """
    token_payload = {TOKEN: {'access_token': raw_jwt, 'token_type': 'bearer'}}
    return bool(safe_get_user(token_payload))


def _configure_server(app, docs_dir: Path) -> None:
    """
    Applies session-cookie security settings and registers /docs Flask routes.
    """
    app.server.secret_key = AUTH.secret_key
    app.server.config['SESSION_COOKIE_HTTPONLY'] = True
    app.server.config['SESSION_COOKIE_SAMESITE'] = 'Strict'
    gunicorn = SETTINGS.dash_settings.gunicorn_setup
    app.server.config['SESSION_COOKIE_SECURE'] = gunicorn

    @app.server.route('/docs')
    def docs_root() -> object:
        """Redirect /docs → /docs/ so relative asset URLs resolve correctly."""
        return redirect(DOCS_URL)

    @app.server.route('/docs/')
    @app.server.route('/docs/<path:path>')
    def serve_docs(path: str = '') -> object:
        """
        Serves built MkDocs files behind a signed HttpOnly session cookie.

        Aborts 503 if docs not built. Unauthenticated requests redirect to /.
        """
        if not docs_dir.is_dir():
            abort(503, 'Documentation not built. Run: make docs-build')

        raw_jwt = flask_session.get(DOCS_SESSION_KEY)
        if raw_jwt and _is_valid_docs_jwt(raw_jwt):
            return send_from_directory(str(docs_dir), _docs_target(path))

        return redirect('/')


def _register_session_sync_callback() -> None:
    """
    Registers the Dash callback syncing the login token into the Flask session.
    """
    @callback(
        Output(DOCS_SYNC, DATA),
        Input(TOKEN, DATA))
    def _sync_docs_session(token_data):
        token = (token_data or {}).get(TOKEN) or {}
        jwt = token.get('access_token')
        if jwt:
            flask_session[DOCS_SESSION_KEY] = jwt
        if not jwt:
            flask_session.pop(DOCS_SESSION_KEY, None)
        return no_update


def enable_flask_docs(app, docs_dir: Path = BASE_PATH / 'docs') -> None:
    """
    Idempotent setup: configures Flask session-cookie security, /docs routes,
    and the Dash TOKEN store → flask_session sync callback.
    """
    app_id = id(app)
    if app_id in _REGISTERED_APPS:
        return
    _REGISTERED_APPS.add(app_id)

    _configure_server(app, docs_dir)
    _register_session_sync_callback()
