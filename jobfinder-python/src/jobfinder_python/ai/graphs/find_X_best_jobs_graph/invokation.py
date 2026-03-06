import uuid
from jobfinder_python.ai.graphs.find_X_best_jobs_graph.graphs import get_find_x_best_jobs_graph
from jobfinder_python.ai.graphs.find_X_best_jobs_graph.states import FindXBestJobsGraphState
from jobfinder_python.api.api_model import FindJobsDto
from jobfinder_python.api.api_model import Job


async def invoke_find_x_best_jobs_graph(input_data: FindJobsDto, input_jobs: list[Job]):
    # init input state
    input_state = FindXBestJobsGraphState(execution_id=str(uuid.uuid4()), input_data=input_data, input_jobs=input_jobs)
    # invoke graph and wait for result
    res = await get_find_x_best_jobs_graph().ainvoke(input=input_state)
    # parse response
    return FindXBestJobsGraphState(**res)
