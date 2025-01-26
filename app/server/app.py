from fastapi import FastAPI
from server.routes.candidate import router as CandidateRouter

app = FastAPI()
app.include_router(CandidateRouter, tags=["Candidate"], prefix="/candidate")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Clay to mongodb collection!"}

