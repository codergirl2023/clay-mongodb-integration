from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import (
    add_candidate
)
from server.models.candidate import (
    ErrorResponseModel,
    ResponseModel,
    CandidateSchema
)

router = APIRouter()

@router.post("/add", response_description="Candidate added into the database")
async def add_candidate_data(candidate: CandidateSchema = Body(...)):
    candidate = jsonable_encoder(candidate)
    new_candidate= await add_candidate(candidate)
    return ResponseModel(new_candidate, "Candidate added successfully.")

