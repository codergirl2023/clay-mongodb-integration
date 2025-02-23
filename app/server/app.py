from fastapi import FastAPI
from server.routes.candidate import router as CandidateRouter
import os
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
load_dotenv()  # Loads environment variables from .env file
app.include_router(CandidateRouter, tags=["Candidate"], prefix="/candidate")

@app.get("/", tags=["Root"])
async def read_root():
    print("mongo db", os.environ.get("MONGO_URI"))
    return {"message": "Clay to mongodb collection!"}
