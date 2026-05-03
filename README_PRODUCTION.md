# BioLinkMS Backend - Production Setup Guide

## 🚀 Production-Ready Features Implemented

### 1. **API Versioning**
- All new API endpoints are under `/api/v1/`
- Backward compatibility maintained with legacy endpoints
- Easy to version future API changes

**Endpoints:**
- `GET /api/v1/health/` - Basic health check
- `GET /api/v1/health/detailed` - Detailed health with DB status
- `GET /api/v1/health/live` - Kubernetes liveness probe
- `GET /api/v1/health/ready` - Kubernetes readiness probe
- `POST /api/v1/auth/register` - User registration
- `POST /api/v1/auth/login` - User login
- `GET /api/v1/auth/me` - Get current user
- `GET /api/v1/tracking/` - Get tracking records
- `POST /api/v1/tracking/` - Create tracking record
- `GET /api/v1/sos/` - Get SOS alerts
- `POST /api/v1/sos/` - Create SOS alert
- `GET /api/v1/logs/` - Get logs

### 2. **Structured Logging**
- JSON format for production (text format for development)
- Includes timestamp, level, service, version, environment
- Supports request ID and user ID tracking
- Configurable log level via environment variables

**Configuration:**
```bash
LOG_LEVEL=INFO  # DEBUG, INFO, WARNING, ERROR, CRITICAL
LOG_FORMAT=json  # json or text
LOG_FILE=/var/log/biolinkms.log  # Optional file path
```

### 3. **Centralized Exception Handling**
- Custom exception classes for common scenarios
- Consistent error response format
- Proper HTTP status codes
- Detailed error logging

**Exception Types:**
- `NotFoundError` - 404
- `AuthenticationError` - 401
- `AuthorizationError` - 403
- `ValidationError` - 422
- `ConflictError` - 409
- `DatabaseError` - 500
- `RateLimitError` - 429

### 4. **Database Migrations (Alembic)**
- Automatic schema evolution
- Support for both SQLite and PostgreSQL
- Version control for database changes

**Setup:**
```bash
# Initialize migrations (already done)
cd backend
alembic upgrade head

# Create new migration
alembic revision --autogenerate -m "Description of changes"

# Apply migrations
alembic upgrade head

# Rollback
alembic downgrade -1
```

### 5. **Comprehensive Testing**
- Pytest with fixtures for database testing
- In-memory SQLite for fast tests
- Test coverage reporting
- Unit and integration test markers

**Run Tests:**
```bash
# Install dev dependencies
pip install -r requirements-dev.txt

# Run all tests
pytest

# Run with coverage
pytest --cov=app

# Run specific test file
pytest tests/test_auth.py

# Run only unit tests
pytest -m unit
```

### 6. **Improved Project Structure**

```
backend/
├── app/
│   ├── api/
│   │   └── v1/                    # API v1 endpoints
│   │       ├── __init__.py
│   │       └── routes/
│   │           ├── __init__.py
│   │           ├── auth.py
│   │           ├── health.py
│   │           ├── tracking.py
│   │           ├── sos.py
│   │           └── logs.py
│   ├── core/                      # Core functionality
│   │   ├── __init__.py
│   │   ├── settings.py            # Configuration
│   │   ├── security.py            # Auth & security
│   │   ├── logging_config.py      # Logging setup
│   │   └── exceptions.py          # Custom exceptions
│   ├── config/
│   │   └── database.py            # Database setup
│   ├── models/                    # SQLAlchemy models
│   ├── schemas/                   # Pydantic schemas
│   ├── auth/                      # Legacy auth (keep for compatibility)
│   ├── routes/                    # Legacy routes (keep for compatibility)
│   └── main.py                    # App entry point
├── alembic/                       # Database migrations
│   ├── versions/
│   ├── env.py
│   └── script.py.mako
├── tests/                         # Test suite
│   ├── __init__.py
│   ├── conftest.py               # Test fixtures
│   ├── test_health.py
│   ├── test_auth.py
│   └── ...
├── alembic.ini                    # Alembic configuration
├── pytest.ini                     # Pytest configuration
├── requirements.txt               # Production dependencies
├── requirements-dev.txt           # Development dependencies
├── Dockerfile                     # Docker image
└── .env.example                   # Environment template
```

## 🛠️ Setup Instructions

### 1. Install Dependencies

```bash
# Production dependencies
pip install -r requirements.txt

# Development dependencies (optional)
pip install -r requirements-dev.txt
```

### 2. Configure Environment

```bash
# Copy example environment file
cp .env.example .env

# Edit .env with your values
# Important: Generate a strong SECRET_KEY
python -c "import secrets; print(secrets.token_urlsafe(64))"
```

### 3. Initialize Database

```bash
# For development (SQLite)
# Database will be created automatically

# For production (PostgreSQL)
# 1. Create database
createdb biolinkms

# 2. Run migrations
alembic upgrade head
```

### 4. Run Tests

```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=app --cov-report=html

# Open coverage report
open htmlcov/index.html  # macOS
xdg-open htmlcov/index.html  # Linux
start htmlcov/index.html  # Windows
```

### 5. Start Application

```bash
# Development (with auto-reload)
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Production
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

### 6. Docker Deployment

```bash
# Build image
docker build -t biolinkms-backend .

# Run container
docker run -d \
  -p 8000:8000 \
  -e DATABASE_URL=postgresql://user:pass@db:5432/biolinkms \
  -e SECRET_KEY=$(python -c "import secrets; print(secrets.token_urlsafe(64))") \
  biolinkms-backend
```

## 📊 Monitoring & Observability

### Health Checks

```bash
# Basic health
curl http://localhost:8000/health

# Detailed health
curl http://localhost:8000/api/v1/health/detailed

# Liveness probe
curl http://localhost:8000/api/v1/health/live

# Readiness probe
curl http://localhost:8000/api/v1/health/ready
```

### Logging

```bash
# View logs (Docker)
docker logs biolinkms-backend

# View logs (systemd)
journalctl -u biolinkms-backend -f

# Filter by level
grep '"level":"ERROR"' /var/log/biolinkms.log
```

## 🔄 Migration Guide

### From Old Structure to New

The application maintains backward compatibility. Old endpoints still work:

- `/api/home` → Use `/api/v1/health/` instead
- `/api/stats` → Deprecated, use specific endpoints
- `/docs` → Still available at `/docs`

### Database Migration

If you have existing data:

```bash
# 1. Backup your database
# SQLite:
cp biolink.db biolink.db.backup

# PostgreSQL:
pg_dump biolinkms > backup.sql

# 2. Run migrations
alembic upgrade head

# 3. Verify data
# Check that all tables and data are intact
```

## 🚨 Troubleshooting

### Migration Issues

```bash
# If migrations fail
alembic stamp head  # Mark current state as latest
alembic upgrade head  # Try again
```

### Test Failures

```bash
# Clear pytest cache
pytest --cache-clear

# Run with verbose output
pytest -vv --tb=long
```

### Import Errors

```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

## 📝 Next Steps

1. **Set up CI/CD** - Automated testing and deployment
2. **Add monitoring** - Prometheus metrics, Sentry error tracking
3. **Implement rate limiting** - Protect against abuse
4. **Add caching** - Redis for sessions and frequent queries
5. **Set up logging aggregation** - ELK stack or similar
6. **Configure backup strategy** - Automated database backups

---

For more information, see:
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Alembic Documentation](https://alembic.sqlalchemy.org/)
- [Pytest Documentation](https://docs.pytest.org/)