#!/bin/bash

# Mood Journal API Setup Script
# This script helps you get started with the project

set -e

echo "🚀 Setting up Mood Journal API..."

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker first."
    echo "   Visit: https://www.docker.com/get-started"
    exit 1
fi

# Check if Docker Compose is installed
if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose is not installed. Please install Docker Compose first."
    exit 1
fi

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo "📝 Creating .env file from template..."
    cp env.example .env
    echo "✅ Created .env file. Please edit it with your configuration."
else
    echo "✅ .env file already exists."
fi

# Install Python dependencies (if Python is available)
if command -v python3 &> /dev/null; then
    echo "📦 Installing Python dependencies..."
    pip3 install -e .
    echo "✅ Python dependencies installed."
else
    echo "⚠️  Python not found. Dependencies will be installed in Docker."
fi

# Build and start services
echo "🐳 Building and starting Docker services..."
docker-compose up --build -d

# Wait for database to be ready
echo "⏳ Waiting for database to be ready..."
sleep 10

# Run migrations
echo "🗄️  Running database migrations..."
docker-compose run --rm migrations

echo ""
echo "🎉 Setup complete!"
echo ""
echo "📋 Next steps:"
echo "1. Edit .env file with your configuration (especially HF_TOKEN for mood extraction)"
echo "2. Visit http://localhost:8000/docs for API documentation"
echo "3. Test the API with: curl http://localhost:8000/api/v1/health"
echo ""
echo "🔧 Useful commands:"
echo "  - View logs: docker-compose logs -f"
echo "  - Stop services: docker-compose down"
echo "  - Restart services: docker-compose restart"
echo "  - Run migrations manually: python scripts/run_migrations.py"
echo ""
echo "📚 Documentation:"
echo "  - README.md - Project overview and quick start"
echo "  - DEVELOPMENT.md - Development guidelines and best practices"
echo "  - spec.md - Project requirements and specifications" 