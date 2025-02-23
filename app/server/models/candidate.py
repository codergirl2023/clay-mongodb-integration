from typing import Optional, List
from pydantic import BaseModel, Field

class CandidateSchema(BaseModel):
    first_name: Optional[str] = Field(default=None)
    last_name: Optional[str] = Field(default=None)
    full_name: Optional[str] = Field(default=None)
    job_title: Optional[str] = Field(default=None)
    location: Optional[str] = Field(default=None)
    company_domain: Optional[str] = Field(default=None)
    linkedin_profile: Optional[str] = Field(default=None)
    enrich_li_profile: Optional[str] = Field(default=None)
    current_company: Optional[str] = Field(default=None)
    summary: Optional[str] = Field(default=None)
    work_experience: Optional[str] = Field(default=None)
    work_experience_response: Optional[str] = Field(default=None)
    education_summary: Optional[str] = Field(default=None)
    education_summary_response: Optional[str] = Field(default=None)
    location_name: Optional[str] = Field(default=None)
    company_industry: Optional[str] = Field(default=None)
    company_industry_result: Optional[str] = Field(default=None)
    skills_keywords: Optional[List[str]] = Field(default=None)  # List of skills or keywords
    skills_keywords_response: Optional[str] = Field(default=None)
    awards_summary: Optional[str] = Field(default=None)
    awards_summary_response: Optional[str] = Field(default=None)
    certifications_summary: Optional[str] = Field(default=None)
    certifications_summary_response: Optional[str] = Field(default=None)
    course_summary: Optional[str] = Field(default=None)
    course_summary_response: Optional[str] = Field(default=None)
    volunteering_summary: Optional[str] = Field(default=None)
    volunteering_summary_response: Optional[str] = Field(default=None)
    patents: Optional[str] = Field(default=None)
    language_summary: Optional[str] = Field(default=None)
    language_summary_response: Optional[str] = Field(default=None)
    github_repositories: Optional[str] = Field(default=None)
    github_repositories_response: Optional[str] = Field(default=None)
    social_media: Optional[str] = Field(default=None)
    social_media_response: Optional[str] = Field(default=None)
    awards_date: Optional[str] = Field(default=None)
    awards_title: Optional[str] = Field(default=None)
    profile_picture: Optional[str] = Field(default=None)

    @classmethod
    def field_names(cls):
        return [
            'First Name', 'Last Name', 'full name', 'Job Title', 'Location',
            'Company Domain', 'LinkedIn URL', 'Current Company', 'Summary',
            'Work Experience', 'Total Experience', 'Github URL', 'Skills', '_id', 'LinkedIn Profile',
            'awards title', 'profile picture', 'awards date'
        ]
    
class CandidateCollection(BaseModel):
    candidates: List[CandidateSchema]
    
def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}