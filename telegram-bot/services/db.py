import motor.motor_asyncio
from motor.motor_asyncio import AsyncIOMotorCollection, AsyncIOMotorClient
from icecream import ic
import os
from dotenv import load_dotenv

load_dotenv()

client : AsyncIOMotorClient = motor.motor_asyncio.AsyncIOMotorClient(os.getenv('MONGO_URL'))


class Collection:
    def __init__(self, collection: AsyncIOMotorCollection):
        self._collection : AsyncIOMotorCollection = collection

    async def create(self, query: dict):
        try:
            result = await self._collection.insert_one(query)
            return result.inserted_id
        except Exception as mongo_create_exception:
            ic(mongo_create_exception)

    async def get(self, query: dict):
        try:
            result = await self._collection.find_one(query)
            return result
        except Exception as mongo_get_exception:
            ic(mongo_get_exception)

    async def edit(self, query: dict, new_data: dict = None):
        """
        $set {'A': 1}  - 'A' = 1
    
        $unset {'A': ''} - remove the 'A' field from a document

        $inc {'A': 1} - 'A' += 1

        $push {'A': 'B'} - add 'B' to the 'A' list

        $pull {'A': 'B'} - remove 'B' from the 'A' list
    
        $addToSet {'A': 'B'} - add 'B' to the 'A' list if it does not already exist

        $pop {'A': 1} - remove the last item from the 'A' list

        $pullAll {'A': ['B', 'C']} - remove multiple items from the 'A' list

        $rename {'A': 'B'} - rename the field 'A' to 'B'
        """
        try:
            await self._collection.update_one(query, new_data)
        except Exception as mongo_edit_exception:
            ic(mongo_edit_exception)

    async def delete(self, query: dict):
        try:
            await self._collection.delete_one(query)
        except Exception as mongo_delete_exception:
            ic(mongo_delete_exception)


db = client.Pokeo
players : Collection = Collection(db.players)
games : Collection = Collection(db.games)
pokemon : Collection = Collection(db.pokemon)