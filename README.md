# Mood Journal API Template

This is a template for a Mood Journal API project using FastAPI (Python) and PostgreSQL, designed for learning backend engineering concepts.

## Features
- FastAPI backend
- PostgreSQL database
- Dockerized app and database
- Health check endpoint (`GET /health`)

## Getting Started

### Prerequisites
- [Docker](https://www.docker.com/get-started)

### Setup
3. Install Python dependencies (locally):
   ```bash
   pip install
   ```
4. Build and start the services:
   ```bash
   docker-compose up --build
   ```
5. The API will be available at [http://localhost:8000](http://localhost:8000)

### Health Check
Test the health endpoint:
```bash
curl http://localhost:8000/health
```
Response:
```json
{"status": "OK"}
```

## Project Structure
- `main.py` - FastAPI app entrypoint
- `Dockerfile` - Containerizes the FastAPI app
- `docker-compose.yml` - Orchestrates app and database
- `pyproject.toml` - Python dependencies and project metadata
