from pydantic import BaseModel, Field


# ---------------------------------------------------------------
# SUB MODEL
# ---------------------------------------------------------------
class BestJob(BaseModel):
    id: str = Field(description="The id of the job")
    reason: str = Field(description="The concise reason why the job is the best for this applicant, in french.")

# ---------------------------------------------------------------
# GRAPH MODEL
# ---------------------------------------------------------------
class FindXBestJobsModel(BaseModel):
    x_best_jobs: list[BestJob] = Field(description="The x best jobs")
