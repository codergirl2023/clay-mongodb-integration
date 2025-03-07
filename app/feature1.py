from fastapi import APIRouter
import pandas as pd
from sentence_transformers import SentenceTransformer, util

router = APIRouter()

# Assuming you have the SBERT model loaded already
sbert_model = SentenceTransformer('bert-base-nli-mean-tokens')

def rank_candidates_simple(candidates_json, job_description, top_n=20):
    """
    Simplified pipeline to rank candidates based on similarity to a job description.
    """
    candidates_df = pd.DataFrame(candidates_json)
    candidates_df = candidates_df.dropna(subset=['Summary', 'Skills'])
    candidates_df['Profile'] = (
        candidates_df['Summary'] + " " +
        candidates_df['Skills']
    )
    
    job_embedding = sbert_model.encode(job_description, convert_to_tensor=True)
    candidate_embeddings = sbert_model.encode(candidates_df['Profile'].tolist(), convert_to_tensor=True)
    
    similarities = util.cos_sim(job_embedding, candidate_embeddings).cpu().tolist()[0]
    candidates_df['Similarity Score'] = similarities
    candidates_df['Rank'] = candidates_df['Similarity Score'].rank(ascending=False, method='dense')
    
    top_candidates = candidates_df.sort_values(by='Rank').head(top_n)
    top_candidates_json = top_candidates.to_json(orient="records", indent=4)
    
    ranked_candidates_json = candidates_json.copy()
    for candidate in ranked_candidates_json:
        candidate_match = candidates_df[candidates_df['_id'] == candidate['_id']]
        if not candidate_match.empty:
            candidate_df = candidate_match.iloc[0]
            candidate["Rank"] = candidate_df["Rank"]    
    return ranked_candidates_json
