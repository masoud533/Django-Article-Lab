# 🧠 Django Blog Lab
A modern Django + DRF powered blog system built for learning advanced workflow.

## 🚀 Stack
- Django 5 / Django REST Framework
- PostgreSQL
- Docker / Docker Compose
- GitHub Actions (for CI)
- Pre-commit hooks (Black, isort, flake8)

## 🧩 Features
- Token-based authentication (DRF)
- CRUD for posts and comments
- User registration/login
- API Documentation (Swagger or drf-spectacular)
- Admin Panel

## ⚙️ Setup
```bash
git clone https://github.com/masoudmapar/django-blog-lab.git
cd django-blog-lab
cp .env.example .env
docker-compose up --build
