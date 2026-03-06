from jobfinder_python.api.api_model import FindJobsDto
from jobfinder_python.ai.graphs.find_X_best_jobs_graph.models import BestJob
from pydantic import BaseModel
from jobfinder_python.api.api_model import Job

class FindXBestJobsGraphState(BaseModel):
    executor_label: str = "find_x_best_jobs_graph"
    # input data
    input_data: FindJobsDto | None = None
    input_jobs: list[Job] | None = None
    x_best_jobs: list[BestJob] | None = None
