
This project uses a **clean Django architecture** with **strict separation**
between **development** and **production** environments.

The setup ensures:
- Development always uses **SQLite**
- Production always uses **PostgreSQL**
- ASGI and WSGI are never mixed
- No manual `DJANGO_SETTINGS_MODULE` configuration is required

---

## 📁 Project Structure

```text
django-best-structer/
├── manage.py
├── .env.example
├── requirements.txt
├── config/
│   ├── asgi.py  # ASGI entry (production)
|   ├── wsgi.py                 
│   ├── urls.py
│   └── settings/
│       ├── base.py
│       ├── local.py         # Development settings (SQLite)
│       └── production.py    # Production settings (PostgreSQL)
├── apps/
│   ├── users/
├── templates/
├── static/
├── staticfiles/
├── media/
├── common/
└── README.md

<!-- LOCAL -->
# Create virtual environment
python -m venv .venv

# Activate virtual environment
source .venv/bin/activate   # macOS / Linux
# .venv\Scripts\activate    # Windows

# Install dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Start development server
python manage.py runserver



<!-- PRODUCTION -->

# Apply database migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic

# Start ASGI server using uvicorn
uvicorn config.asgi:application --bind 0.0.0.0:9000# django-folder-structer
