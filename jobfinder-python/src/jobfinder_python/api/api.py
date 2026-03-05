from jobfinder_python.logging.logging import app_logger
from fastapi import APIRouter
from jobfinder_python.api.api_model import FindJobsDto, FindJobsResponse
from jobfinder_python.service.find_jobs import find_jobs

router = APIRouter(prefix="/jobfinder", tags=["JobFinder"])


@router.post(
    "/find_jobs",
    response_model=FindJobsResponse,
)
async def api_find_jobs(find_jobs_dto: FindJobsDto):
    try:
        result = await find_jobs(find_jobs_dto)
        return result
    except Exception as e:
        app_logger.error(f"Error invoking my example graph: {e}")
        raise e
