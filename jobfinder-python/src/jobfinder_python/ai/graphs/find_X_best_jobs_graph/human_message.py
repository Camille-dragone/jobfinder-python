from jobfinder_python.ai.graphs.find_X_best_jobs_graph.models import FindXBestJobsModel
from langchain_core.messages import HumanMessage
from jobfinder_python.ai.graphs.find_X_best_jobs_graph.prompts import get_start_prompt, get_middle_prompt, get_end_prompt
from jobfinder_python.api.api_model import Job
from fastapi import UploadFile


async def get_human_message(description: str, jobs: list[Job], cv: UploadFile, X: int):
    human_message_content = []

    # build prompt
    prompt = get_start_prompt(description, X)
    prompt += get_middle_prompt(jobs)
    # add applicant CV

    prompt += get_end_prompt()
    human_message_content.append(prompt)

    # build human message from prompt
    human_message = HumanMessage(
        content="\n".join(human_message_content),
        # config={
        #     "response_mime_type": "application/json",
        #     "response_schema": FindXBestJobsModel,
        # },
    )
    return human_message
