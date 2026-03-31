# Django + DRF Skeleton

This is a minimal Django + Django REST Framework (DRF) starter with a single
`Task` API and a clean project layout.

## Quick Start

1. Create and activate a virtualenv:
```bash
python -m venv .venv
source .venv/bin/activate
```

1. Install dependencies:
```bash
pip install -r requirements.txt
```

1. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

1. Start the server:
```bash
python manage.py runserver
```

The API will be available at:

- `GET /api/tasks/`
- `POST /api/tasks/`
- `GET /api/tasks/<id>/`
- `PATCH /api/tasks/<id>/`
- `DELETE /api/tasks/<id>/`

## Project Structure

- `manage.py`: Django management commands.
- `config/`: Project settings and root URLs.
- `api/`: Example app with a `Task` model, serializer, and viewset.
- `requirements.txt`: Django + DRF dependencies.
