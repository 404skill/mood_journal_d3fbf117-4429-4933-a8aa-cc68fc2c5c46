# Mood Journal API - Minimal FastAPI Template

A minimal FastAPI starter template with database connection, health endpoint, and migration support.

## 🚀 Quick Start

### Run with Docker Compose

```bash
# Start everything (app + database)
docker-compose up --build

# Or run in background
docker-compose up -d --build
```

The API will be available at http://localhost:8000

### Run Locally (for development)

```bash
# Start only the database
docker-compose up -d db

# Install dependencies
pip install -e .

# Run the application
python -m app.main
```

The API will be available at http://localhost:8000

## 🧪 Testing

```bash
# Test health endpoint
curl http://localhost:8000/health

# Expected response:
# {"status": "healthy", "database": "connected"}
```

## 📁 Project Structure

```
app/
├── __init__.py
├── main.py              # FastAPI app with health endpoint
└── database.py          # Database connection & session management
```

---

**Ready to build! 🎉**
