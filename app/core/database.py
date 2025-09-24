# app/core/database.py
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from typing import Optional
from app.core.config import settings


class DatabaseConnection:
    """Singleton Pattern for Database Connection Management

    This pattern ensures that we only have one connection to MongoDB.
    Advantages:
    1. Resource saving
    2. Centralized connection management
    """

    _instance: Optional['DatabaseConnection'] = None
    _client: Optional[AsyncIOMotorClient] = None
    _database: Optional[AsyncIOMotorDatabase] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
        return cls._instance

    async def connect(self):
        """making connection to database"""
        if self._client is None:
            self._client = AsyncIOMotorClient(settings.MONGODB_URL)
            self._database = self._client[settings.DATABASE_NAME]
            print("[OK] Connected to MongoDB")
    async def disconnect(self):
        """disconnecting from database"""
        if self._client:
            self._client.close()
            self._client = None
            self._database = None
            print("[X] Disconnected from MongoDB")

    @property
    def database(self) -> AsyncIOMotorDatabase:
        """accessing database instance"""
        if self._database is None:
            raise RuntimeError("Database is not connected")
        return self._database


# Instance global
db_connection = DatabaseConnection()