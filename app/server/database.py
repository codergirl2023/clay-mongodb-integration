import motor.motor_asyncio
from config.settings import settings
from pymongo.errors import PyMongoError
from bson import ObjectId
from fastapi import HTTPException

DATABASE_URL = settings.DB_URL

client = motor.motor_asyncio.AsyncIOMotorClient(DATABASE_URL)
database = client.LookoutAI

collection = database.get_collection("candidates")

async def add_candidate(candidate_data: dict) -> dict:
    try:
        await collection.insert_one(candidate_data)
        return {"message": "Candidate received"}
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")

async def list_candidates(chatbox_id):
    try:
        # Fetch candidates from MongoDB
       
        candidates = await collection.find({'Chatbox ID': chatbox_id}).to_list(length=5)
        serialized_candidates = []
        # Serialize each candidate document
        for candidate in candidates:
            serialized_candidate = {}
            for key, value in candidate.items():
                if isinstance(value, ObjectId):
                    serialized_candidate[key] = str(value)
                else:
                    serialized_candidate[key] = value
           
            serialized_candidates.append(serialized_candidate)
        return serialized_candidates

    except PyMongoError as e:
        return {"error": f"An error occurred with MongoDB: {str(e)}"}

    except Exception as e:
        return {"error": f"An unexpected error occurred: {str(e)}"}
    
async def delete_candidates():
    await collection('inventory').deleteMany({});