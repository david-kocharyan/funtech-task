# Reward Platform API

Backend API for managing users, rewards, and scheduled tasks using Django, Celery, PostgreSQL, and Redis.

---

## Requirements

- Python 3.12
- PostgreSQL
- Redis
- Docker & Docker Compose

---

## Local Setup

1. **Clone the repository**

```bash
  git clone https://github.com/your-username/your-repo.git
```

```bash
  cd funtech_task
```

2. **Create and activate virtual environment**

```bash
  python3.12 -m venv venv
```

```bash
  source venv/bin/activate
```

3. **Install dependencies**

```bash
  pip install -r requirements.txt
```

4. **Set environment variables**

Copy .env.example to .env and fill in values.

5. **Apply migrations & run server**

```bash
  python manage.py migrate
```

```bash
  python manage.py runserver
```

6. **Start Celery worker (in a separate terminal)**

```bash
  celery -A funtech worker --loglevel=info
```

7. **(Optional) Start Celery beat**

```bash
  celery -A funtech beat --loglevel=info
```

## 🐳 Docker Setup

The `docker-compose.yml` includes the following services:

- `web`: Django app (ASGI-based)
- `db`: PostgreSQL 15
- `redis`: Redis 7 (Celery broker)
- `celery`: Worker for background tasks

Make sure you have a `.env` file based on `.env.example` with correct values.

```bash
# 1. Build and start all containers
docker-compose up --build

# 2. Run database migrations
docker-compose exec web python manage.py migrate

# 3. (Optional) Create a Django superuser
docker-compose exec web python manage.py createsuperuser
```

## Note

* After startup, your Django app will be available at: [http://localhost:8000](http://localhost:8000)
* You can access Swagger docs at: [http://localhost:8000/swagger/](http://localhost:8000/swagger/)
* You can access Admin dashboard at: [http://localhost:8000/admin/](http://localhost:8000/admin/)