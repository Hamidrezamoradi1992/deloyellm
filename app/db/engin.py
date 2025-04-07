from typing import Optional
from beanie import init_beanie, Document
from motor.motor_asyncio import AsyncIOMotorClient


class MongoDBHandler:
    def __init__(self, uri: str, db_name: str, document_models: list[Document]):
        self.uri = uri
        self.db_name = db_name
        self.client: Optional[AsyncIOMotorClient] = None
        self.document_models = document_models

    async def connect(self):
        self.client = AsyncIOMotorClient(self.uri)
        await init_beanie(database=self.client[self.db_name], document_models=self.document_models)

    async def close(self):
        if self.client:
            self.client.close()
