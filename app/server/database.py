import motor.motor_asyncio
from .settings import mongo_settings as settings

MONGO_DETAILS = settings.uri

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.lookoutai

collection = database.get_collection("candidates")

async def add_candidate(candidate_data: dict) -> dict:
    try:
        # Insert the candidate data into the database
        candidate = await collection.insert_one(candidate_data)
        
        # Return a success message
        return {"message": "Candidate received"}
    
    except motor.motor_asyncio.errors.PyMongoError as e:
        # Catch any errors from MongoDB
        return {"error": f"An error occurred with MongoDB: {str(e)}"}
    
    except Exception as e:
        # Catch any other unexpected errors
        return {"error": f"An unexpected error occurred: {str(e)}"}
