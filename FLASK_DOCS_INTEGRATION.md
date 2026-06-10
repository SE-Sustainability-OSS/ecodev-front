# Flask-Served MkDocs Integration

This document describes the reusable "Flask-served MkDocs behind JWT" pattern provided by
`ecodev-front`. It covers how the system works, the security model, and a step-by-step adoption
guide for any new Dash app.

**Reference implementation:** `ecoact-natwest`

---

## How it works

### Overview

MkDocs documentation is built into the Docker image at build time and served by the Dash app's own
Flask server on the same port and domain under the `/docs/` prefix. Access is gated by the same JWT
used for the Dash app. No extra container, subdomain, or auth system is required.

```
┌─────────────────────────────────────────────────────────────┐
│  Docker Image (single container)                            │
│                                                             │
│  ┌──────────────┐   COPY /app/docs   ┌──────────────────┐  │
│  │ docs-builder │ ────────────────►  │ Final image      │  │
│  │ mkdocs build │                    │ /app/docs/       │  │
│  └──────────────┘                    │ (static HTML)    │  │
│                                      └──────────────────┘  │
└─────────────────────────────────────────────────────────────┘

Browser                        Flask (same port 80)
  │                                    │
  ├─ Dash login callback ─────────────►│  sets flask_session[DOCS_SESSION_KEY] = jwt
  │                                    │
  ├─ GET  /docs/         ─────────────►│  reads session cookie → validates → send_from_directory
  │                                    │
  └─ Dash logout callback ────────────►│  flask_session.pop(DOCS_SESSION_KEY)
```

### The `with_docs()` flag

Everything is activated by a single config flag in your app's settings:

```yaml
# config/local.yaml (or any environment config)
dash_settings:
  with_docs: true
```

`with_docs()` in `ecodev_front.flask_docs` reads this defensively:

```python
def with_docs() -> bool:
    return getattr(SETTINGS.dash_settings, 'with_docs', False)
```

Apps without the flag default to `False` without error.

### `dash_base_layout` → `enable_flask_docs` hook

When `dash_base_layout(...)` is called during app initialisation, it checks `with_docs()`:

- If `True`: adds a hidden `dcc.Store(id=DOCS_SYNC)` to the AppShell layout and calls
  `enable_flask_docs(dash.get_app())`.
- If `False`: no-op — the regular `documentation_icon_link` is used in the header instead.

`enable_flask_docs` is **idempotent**: it tracks registered app IDs and skips re-registration on
Dash hot-reload or repeated layout builds.

### `/docs` Flask routes

`enable_flask_docs` registers two Flask routes:

| Route | Behaviour |
|-------|-----------|
| `GET /docs` | Redirects to `/docs/` so relative asset URLs resolve correctly |
| `GET /docs/` and `GET /docs/<path:path>` | Validates JWT session cookie; serves static file via `send_from_directory`; aborts 503 if docs not built; redirects to `/` if unauthenticated |

Path resolution (`_docs_target`): empty path → `index.html`; paths with an extension → served as-is;
paths without extension → `path/index.html`.

### Session-cookie security model

`enable_flask_docs` applies the following to `app.server` before registering routes:

```python
app.server.secret_key = AUTH.secret_key
app.server.config['SESSION_COOKIE_HTTPONLY'] = True
app.server.config['SESSION_COOKIE_SAMESITE'] = 'Strict'
app.server.config['SESSION_COOKIE_SECURE'] = SETTINGS.dash_settings.gunicorn_setup
```

| Setting | Value | Explanation |
|---------|-------|-------------|
| `secret_key` | `AUTH.secret_key` | Signs the session cookie with HMAC. Required for `flask.session`. Comes from `ecodev_core` auth config. |
| `SESSION_COOKIE_HTTPONLY` | `True` | JavaScript cannot read this cookie (`document.cookie`). Prevents session theft via XSS. |
| `SESSION_COOKIE_SAMESITE` | `'Strict'` | Cookie is only sent when the request originates from the same site. Prevents CSRF. |
| `SESSION_COOKIE_SECURE` | `gunicorn_setup` bool | When `True` (production), cookie is only sent over HTTPS. `False` in local dev. |

`flask_session` is a request-scoped proxy to Flask's built-in signed cookie session
(`SecureCookieSession`). The entire session state lives in a signed cookie; tampering is detected
server-side; `HttpOnly` means JavaScript never sees the value.

### Threat model

| Threat | Mitigation |
|--------|-----------|
| Unauthenticated access to `/docs/*` | Every request re-validates the JWT; unauthenticated requests redirect to `/` |
| XSS stealing the session cookie | `SESSION_COOKIE_HTTPONLY = True` |
| CSRF forcing a request with a stolen cookie | `SESSION_COOKIE_SAMESITE = 'Strict'` |
| Cookie interception over HTTP | `SESSION_COOKIE_SECURE = True` in production |
| Expired or revoked JWT in session | `_is_valid_docs_jwt` calls `safe_get_user` on every `/docs/*` request |
| Cookie forgery | Cookie is signed with `AUTH.secret_key` (HMAC); tampering is detected by Werkzeug |

### `TOKEN` store → `flask_session` sync callback

A server-side Dash callback is registered by `enable_flask_docs`:

```python
@callback(Output(DOCS_SYNC, DATA), Input(TOKEN, DATA))
def _sync_docs_session(token_data):
    jwt = (token_data or {}).get(TOKEN, {}).get('access_token')
    if jwt:
        flask_session[DOCS_SESSION_KEY] = jwt
    if not jwt:
        flask_session.pop(DOCS_SESSION_KEY, None)
    return no_update
```

This callback fires whenever the `TOKEN` store changes (login or logout). Because Dash Python
callbacks run inside a Flask request context, `flask.session` is fully writable here — no separate
Flask routes or JavaScript are needed. Flask automatically includes a `Set-Cookie` response header
when the session is modified.

### Why a signed HttpOnly cookie (and not a clientside_callback)?

- **Works across gunicorn workers**: the signed cookie is sent by the browser on every request;
  any worker can validate it without shared in-memory state.
- **JavaScript cannot read it**: `HttpOnly` blocks `document.cookie` access entirely, eliminating
  XSS-based session theft.
- **No extra endpoints**: the session lifecycle is managed entirely by the existing Python login
  callback, with no `/docs/set-auth` route or `clientside_callback` required.

---

## What is automatic vs. what you must add per repo

### AUTOMATIC (provided by `ecodev-front` when `with_docs: true`)

- Flask routes `/docs` and `/docs/<path:path>` (registered by `enable_flask_docs`)
- Session-cookie security settings on `app.server`
- `TOKEN` → `flask_session` sync Dash callback
- Documentation button in the app header (`flask_docs_link` via `display_app_header`)
- Hidden `dcc.Store(id=DOCS_SYNC)` in the base layout

### REPO-LOCAL (you must add in the consuming app)

- Docker `docs-builder` stage copying built site to `/app/docs`
- `mkdocs.yml` + `mkdocs/` markdown content + `mkdocs/stylesheets/extra.css`
- `.gitignore` entries for `/docs/` and `/site/`
- `docs-build` and `docs-serve` Makefile targets
- `dash_settings.with_docs: true` in the app config

---

## Adoption guide

### Step 1 — Enable the flag

In your app config (e.g. `config/local.yaml` and `config/production.yaml`):

```yaml
dash_settings:
  with_docs: true
```

No changes to `dash_app.py` are needed. `dash_base_layout` picks up the flag automatically.

### Step 2 — Use `display_app_header` from `ecodev-front`

In your header/access callback, use the standard `display_app_header` from `ecodev_front`.
When `with_docs()` is `True`, the documentation button automatically points to `/docs/`.

```python
from ecodev_front import display_app_header

# Optional: pass extra_action_items for custom right-side header buttons
return display_app_header(pathname, module_items, APP_NAME, extra_action_items=[my_button])
```

The `with_flask_docs` parameter is now optional: when `None` (default), it is resolved via
`with_docs()`. You can still pass `with_flask_docs=True` explicitly for backward compatibility.

### Step 3 — Dockerfile docs-builder stage

Add a `docs-builder` stage before the final image in `Dockerfile` (and `Dockerfile-dev`):

```dockerfile
##########
# DOCS   #
##########
FROM python:3.11-slim AS docs-builder
RUN python3 -m pip install --no-cache-dir mkdocs-material
COPY mkdocs.yml /app/mkdocs.yml
COPY mkdocs/ /app/mkdocs/
WORKDIR /app
RUN mkdocs build
```

In the final stage, copy the built output:

```dockerfile
COPY --from=docs-builder /app/docs /app/docs
```

`mkdocs-material` does **not** need to be in `requirements.txt` — it is only needed at build time.

### Step 4 — mkdocs.yml + markdown content

Place `mkdocs.yml` at the **repo root**:

```yaml
site_name: My App Documentation
dev_addr: 0.0.0.0:10021
docs_dir: mkdocs
site_dir: docs

theme:
  name: material
  palette:
    - scheme: default
      primary: custom
      accent: custom
  features:
    - navigation.tabs
    - navigation.sections
    - navigation.top
    - content.code.copy
    - toc.follow

extra_css:
  - stylesheets/extra.css
```

Add `mkdocs/stylesheets/extra.css`:

```css
:root > * {
  --md-primary-fg-color:        #007A27;
  --md-primary-fg-color--light: #4FD267;
  --md-primary-fg-color--dark:  #00682b;
  --md-accent-fg-color:         #1FB144;
  --md-accent-fg-color--transparent: #00351D;
}
```

Add your markdown pages under `mkdocs/`.

### Step 5 — .gitignore

```gitignore
# MkDocs build output
/docs/
/site/
```

### Step 6 — Makefile targets

```makefile
docs-build:    ##@docs Build the MkDocs static site into docs/
	mkdocs build

docs-serve:    ##@docs Serve docs locally at localhost:10021
	mkdocs serve -a 0.0.0.0:10021
```

`make docs-serve` serves without authentication — JWT auth only applies to the Flask-served
`/docs/` route inside the running Dash container.

---

## Reference: `ecoact-natwest`

`ecoact-natwest` is the reference worked example implementing this pattern. It demonstrates:

- `dash_settings.with_docs: true` in config
- Dockerfile multi-stage `docs-builder` stage
- `mkdocs.yml` with material theme and custom EcoAct colours
- Markdown sources under `mkdocs/`
- `display_app_header` from `ecodev-front` with no extra session wiring

Compare its implementation against the steps above to resolve any integration questions.
