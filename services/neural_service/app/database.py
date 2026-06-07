from motor.motor_asyncio import AsyncIOMotorClient

MONGODB_URL = "mongodb://mongodb:27017"
client = AsyncIOMotorClient(MONGODB_URL)
db = client.neural_db