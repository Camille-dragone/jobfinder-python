from pydantic import BaseModel
from fastapi import UploadFile
from typing import Any

class FindJobsDto(BaseModel):
    job_title: str
    job_location: str
    applicant_description: str
    cv: UploadFile

class Job(BaseModel):
    title: str
    company: str
    description: str
    url: str
    source: str
    location: str | None = None
    salary: str | None = None
    posted_date: str | None = None
    company_logo: str | None = None
    company_url: str | None = None
    company_description: str | None = None
    extensions: list[str] | None = None
    raw: Any

class FindJobsResponse(BaseModel):
    jobs: list[Job]
