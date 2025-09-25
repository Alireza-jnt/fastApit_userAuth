from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional, List, Dict, Any
from motor.motor_asyncio import AsyncIOMotorDatabase
from bson import ObjectId

T = TypeVar('T')


class BaseRepository(ABC, Generic[T]):
    """Repository Pattern - Abstract Base Repository

    This pattern abstracts database access.
    Advantages:
    1. Separates business logic from data access
    2. Better testability
    3. Allows database changes without changing business logic
    """

    def __init__(self, database: AsyncIOMotorDatabase, collection_name: str):
        self.database = database
        self.collection = database[collection_name]

    async def create(self, document: Dict[str, Any]) -> T:
        """Creating a new document"""
        result = await self.collection.insert_one(document)
        document["_id"] = result.inserted_id
        return self._document_to_model(document)

    async def find_by_id(self, id: str) -> Optional[T]:
        document = await self.collection.find_one({"_id": ObjectId(id)})
        return self._document_to_model(document) if document else None

    async def find_one(self, filter: Dict[str, Any]) -> Optional[T]:
        """Finding one document"""
        document = await self.collection.find_one(filter)
        return self._document_to_model(document) if document else None

    async def find_many(self, filter: Dict[str, Any] = {}) -> List[T]:
        """Finding multiple documents"""
        cursor = self.collection.find(filter)
        documents = await cursor.to_list(length=None)
        return [self._document_to_model(doc) for doc in documents]

    async def update(self, id: str, update_data: Dict[str, Any]) -> Optional[T]:
        """Updating one document"""
        result = await self.collection.find_one_and_update(
            {"_id": ObjectId(id)},
            {"$set": update_data},
            return_document=True
        )
        return self._document_to_model(result) if result else None

    async def delete(self, id: str) -> bool:
        """removing a document"""
        result = await self.collection.delete_one({"_id": ObjectId(id)})
        return result.deleted_count > 0

    @abstractmethod
    def _document_to_model(self, document: Dict[str, Any]) -> T:
        """Convert document to model

        This method must be implemented in every repository
        """
        pass
