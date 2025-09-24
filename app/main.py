from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.core.config import settings
from app.core.database import db_connection

@asynccontextmanager
async def lifespan(app: FastAPI):
    """managing project lifecycle"""
    # Startup
    await db_connection.connect()
    yield
    # Shutdown
    await db_connection.disconnect()
app = FastAPI(
    title=settings.PROJECT_NAME,
    version="1.0.0",
    lifespan=lifespan
)


@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "message": "Auth System API",
        "version": "1.0.0",
        "status": "healthy"
    }

@app.get("/health")
async def health_check():
    """Checking the service and database"""
    try:
        # database connection test
        await db_connection.database.command("ping")
        return {
            "status": "healthy",
            "database": "connected"
        }
    except Exception as e:
        return {
            "status": "unhealthy",
            "database": "disconnected",
            "error": str(e)
        }