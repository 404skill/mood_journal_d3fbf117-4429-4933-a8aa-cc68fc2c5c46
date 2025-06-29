#!/usr/bin/env python3
"""
Database migration runner.

This script applies SQL migrations to the database.
"""

import asyncio
import os
import sys
from pathlib import Path
from sqlalchemy.ext.asyncio import create_async_engine
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database configuration
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+asyncpg://journal_user:journal_pass@localhost:5432/journal_db"
)

async def run_migrations():
    """
    Run all migration files in order.
    """
    # Create engine
    engine = create_async_engine(DATABASE_URL, echo=True)
    
    try:
        async with engine.begin() as conn:
            # Create migrations table if it doesn't exist
            await conn.execute("""
                CREATE TABLE IF NOT EXISTS migrations (
                    id SERIAL PRIMARY KEY,
                    filename VARCHAR(255) NOT NULL UNIQUE,
                    applied_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
                )
            """)
            
            # Get migration files
            migrations_dir = Path(__file__).parent.parent / "migrations"
            migration_files = sorted([
                f for f in migrations_dir.glob("*.sql")
                if f.name != "__init__.py"
            ])
            
            print(f"Found {len(migration_files)} migration files")
            
            for migration_file in migration_files:
                # Check if migration already applied
                result = await conn.execute(
                    "SELECT id FROM migrations WHERE filename = %s",
                    (migration_file.name,)
                )
                
                if result.fetchone():
                    print(f"Skipping {migration_file.name} (already applied)")
                    continue
                
                # Read and execute migration
                print(f"Applying {migration_file.name}...")
                with open(migration_file, 'r') as f:
                    migration_sql = f.read()
                
                # Split by semicolon and execute each statement
                statements = [stmt.strip() for stmt in migration_sql.split(';') if stmt.strip()]
                
                for statement in statements:
                    if statement:
                        await conn.execute(statement)
                
                # Record migration as applied
                await conn.execute(
                    "INSERT INTO migrations (filename) VALUES (%s)",
                    (migration_file.name,)
                )
                
                print(f"Applied {migration_file.name}")
            
            print("All migrations completed successfully!")
            
    except Exception as e:
        print(f"Migration failed: {e}")
        sys.exit(1)
    finally:
        await engine.dispose()

if __name__ == "__main__":
    asyncio.run(run_migrations()) 