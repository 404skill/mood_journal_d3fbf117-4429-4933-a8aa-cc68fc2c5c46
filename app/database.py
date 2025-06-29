"""
Database configuration for the Mood Journal API.
"""

import os
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy import text
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database configuration
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+asyncpg://journal_user:journal_pass@localhost:5432/journal_db"
)

# Engine configuration
engine = create_async_engine(
    DATABASE_URL,
    echo=False,
    pool_pre_ping=True,
    pool_recycle=3600,
    pool_size=10,
    max_overflow=20,
)

# Session factory
AsyncSessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """Dependency to get database session."""
    async with AsyncSessionLocal() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()

async def init_db():
    """Initialize database tables."""
    # TODO: Import and create your models here
    # Example:
    # from app.models import Base
    # async with engine.begin() as conn:
    #     await conn.run_sync(Base.metadata.create_all)
    print("Database initialization ready - implement your models first!")

async def close_db():
    """Close database connections."""
    await engine.dispose()

async def check_db_health() -> bool:
    """Check if database is accessible."""
    try:
        async with engine.begin() as conn:
            await conn.execute(text("SELECT 1"))
        return True
    except Exception:
        return False