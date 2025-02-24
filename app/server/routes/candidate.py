from fastapi import APIRouter, Body, HTTPException
from fastapi.encoders import jsonable_encoder
from rankingAlgorithm import rank_candidates_simple
import json
from server.database import (
    add_candidate,
    list_candidates,
    delete_candidates
)
from server.models.candidate import (
    ErrorResponseModel,
    ResponseModel,
    CandidateSchema
)

router = APIRouter()

@router.post("/add", response_description="Candidate added into the database")
async def add_candidate_data(candidate: CandidateSchema = Body(...)):
    try:
        candidate = jsonable_encoder(candidate)
        new_candidate= await add_candidate(candidate)
        return ResponseModel(new_candidate, "Candidate added successfully.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}") 

@router.get("/get-search-results", response_description="Candidates Search results returned from the database")
async def get_search_results():
    candidates = await list_candidates()
    try:
        candidates_json_ranked = rank_candidates_simple(candidates, "Software engineer with 5 years of experience", 20)
        
        return candidates_json_ranked
    except Exception as e:
        print(f"Error occurred: {e}")
    
    # return candidates

@router.delete("/deleteAll", response_description="Delete all candidates")
async def delete_all_candidates():
    result = await delete_candidates()
    return ResponseModel(result.deletedCount, "Deleted all candidates")