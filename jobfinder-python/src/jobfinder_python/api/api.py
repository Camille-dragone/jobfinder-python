from jobfinder_python.logging.logging import app_logger
from fastapi import APIRouter
from jobfinder_python.api.api_model import FindJobsDto, FindJobsResponse, Job
from jobfinder_python.service.find_jobs import find_jobs
from fastapi import Form, UploadFile, File
from typing import Any, List

router = APIRouter(prefix="/jobfinder", tags=["JobFinder"])


@router.post(
    "/find_jobs",
    response_model=List[Job],
)
async def api_find_jobs(
    job_title: str = Form(...),
    job_location: str = Form(...),
    applicant_description: str = Form(...),
    cv: UploadFile = File(...),
):
    app_logger.info(f"API find_jobs called with job_title: {job_title}, job_location: {job_location}, applicant_description: {applicant_description}, cv: {cv.filename}")
    find_jobs_dto = FindJobsDto(
        job_title=job_title,
        job_location=job_location,
        applicant_description=applicant_description,
        cv=cv,
    )
    try:
        result = find_jobs(find_jobs_dto)
        return result
    except Exception as e:
        app_logger.error(f"Error invoking my example graph: {e}")
        raise e
