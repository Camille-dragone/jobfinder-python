from jobfinder_python.ai.graphs.find_X_best_jobs_graph.models import FindXBestJobsModel
from jobfinder_python.api.api_model import Job, BestJobResponse

def merge_best_jobs(x_best_jobs_response: FindXBestJobsModel, jobs: list[Job]):
    x_best_jobs = x_best_jobs_response.x_best_jobs
    best_jobs_result = []
    for best_job in x_best_jobs:
        for job in jobs:
            if job.uuid == best_job.id:
                best_jobs_result.append(BestJobResponse(job=job, reason=best_job.reason))
                break
    return best_jobs_result