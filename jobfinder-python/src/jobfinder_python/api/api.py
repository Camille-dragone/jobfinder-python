from jobfinder_python.logging.logging import app_logger
from fastapi import APIRouter
from jobfinder_python.api.api_model import FindJobsDto, BestJobResponse
from jobfinder_python.service.find_jobs import find_jobs
from fastapi import Form, UploadFile, File
from typing import List
from jobfinder_python.ai.graphs.find_X_best_jobs_graph.invokation import invoke_find_x_best_jobs_graph
from jobfinder_python.service.merge_jobs import merge_best_jobs
from jobfinder_python.ai.graphs.help_for_apply_graph.invokation import invoke_help_for_apply_graph
from jobfinder_python.api.api_model import HelpForApplyDto
from jobfinder_python.ai.graphs.help_for_apply_graph.models import HelpForApplyModel

router = APIRouter(prefix="/jobfinder", tags=["JobFinder"])


@router.post(
    "/find_jobs",
    response_model=List[BestJobResponse],
)
async def api_find_jobs(
    job_title: str = Form(...),
    job_location: str = Form(...),
    applicant_description: str = Form(...),
    cv: UploadFile = File(...),
    X: int = Form(1),
):
    app_logger.info(f"API find_jobs called with job_title: {job_title}, job_location: {job_location}, applicant_description: {applicant_description}, cv: {cv.filename}")
    find_jobs_dto = FindJobsDto(
        job_title=job_title,
        job_location=job_location,
        applicant_description=applicant_description,
        cv=cv,
        X=X,
    )
    try:
        result = find_jobs(find_jobs_dto)
        x_best_jobs_response = await invoke_find_x_best_jobs_graph(find_jobs_dto, result)
        x_best_jobs = merge_best_jobs(x_best_jobs_response, result)
        return x_best_jobs[:X] if len(x_best_jobs) > X else x_best_jobs
    except Exception as e:
        app_logger.error(f"Error invoking find_x_best_jobs_graph: {e}")
        raise e


@router.post(
    "/help_for_apply",
    response_model=HelpForApplyModel,
)
async def api_help_for_apply(
    job_title: str = Form(...),
    job_description: str = Form(...),
    job_extensions: list[str] = Form(...),
    applicant_description: str = Form(...),
    cv: UploadFile = File(...)
):
    app_logger.info(f"API help_for_apply called with job_title: {job_title}, job_description: {job_description}, job_extensions: {job_extensions}, applicant_description: {applicant_description}, cv: {cv.filename}")
    help_for_apply_dto = HelpForApplyDto(
        job_title=job_title,
        job_description=job_description,
        job_extensions=job_extensions,
        applicant_description=applicant_description,
        cv=cv,
    )
    try:
        help_for_apply_response = await invoke_help_for_apply_graph(help_for_apply_dto)
        return help_for_apply_response.help_for_apply
    except Exception as e:
        app_logger.error(f"Error invoking help_for_apply_graph: {e}")
        raise e
