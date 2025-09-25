from typing import Optional, Dict, Any
from app.repositories.base import BaseRepository
from app.models.user import User


class UserRepository(BaseRepository[User]):
    """Repository for managing users in the database"""

    def __init__(self, database):
        super().__init__(database, "users")

    async def find_by_email(self, email: str) -> Optional[User]:
        return await self.find_one({"email": email})

    async def find_by_username(self, username: str) -> Optional[User]:
        return await self.find_one({"username": username})

    async def find_by_username_or_email(self, username_or_email: str) -> Optional[User]:
        return await self.find_one({
            "$or": [
                {"username": username_or_email},
                {"email": username_or_email}
            ]
        })

    def _document_to_model(self, document: Dict[str, Any]) -> User:
        """Converting document to User model"""
        if document:
            document["id"] = str(document.pop("_id", None))
        return User(**document)
