from pydantic import BaseModel
from fastapi import UploadFile
from typing import Any

class FindJobsDto(BaseModel):
    job_title: str
    job_location: str
    applicant_description: str
    cv: UploadFile
    X: int = 10

class ApplyOption(BaseModel):
    title: str
    link: str

class Job(BaseModel):
    uuid: str
    title: str
    company: str
    description: str
    url: str
    source: str
    location: str | None = None
    company_logo: str | None = None
    extensions: list[str] | None = None
    apply_options: list[ApplyOption] | None = None
    # raw: Any # to debug

class FindJobsResponse(BaseModel):
    jobs: list[Job]

class BestJobResponse(BaseModel):
    job: Job
    reason: str