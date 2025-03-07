from fastapi import APIRouter, Body, HTTPException
from fastapi.encoders import jsonable_encoder
from feature1 import rank_candidates_simple
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

@router.post("/get-search-results", response_description="Candidates Search results returned from the database")
async def get_search_results(search_query:dict = Body(...)):
    search_query_stringify = json.dumps(search_query)
    chatbox_id = search_query.get("chatbox", {}).get("id")

    if chatbox_id is None:
        raise HTTPException(status_code=400, detail="Chatbox ID is missing")

    candidates = await list_candidates(chatbox_id)
    if candidates is None or not candidates:
        raise HTTPException(status_code=404, detail="No candidates found")

    try:
        candidates_json_ranked = rank_candidates_simple(candidates, search_query_stringify, 5)
        candidates_json_ranked.sort(key=lambda x: x.get('Rank', 0))
        return candidates_json_ranked
    except Exception as e:
        print(f"Error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    

@router.delete("/deleteAll", response_description="Delete all candidates")
async def delete_all_candidates():
    result = await delete_candidates()
    return ResponseModel(result.deletedCount, "Deleted all candidates")