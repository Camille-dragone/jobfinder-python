import os
from jobfinder_python.ai.graphs.find_X_best_jobs_graph.states import FindXBestJobsGraphState
from jobfinder_python.ai.graphs.find_X_best_jobs_graph.models import FindXBestJobsModel
from jobfinder_python.logging.logging import app_logger
from jobfinder_python.ai.graphs.common.ai_utils import get_llm_abstraction
from jobfinder_python.ai.graphs.find_X_best_jobs_graph.human_message import get_human_message


async def find_x_best_jobs_node(state: FindXBestJobsGraphState):
    app_logger.info(f"-- {state.executor_label} | find_x_best_jobs_node()")

    # get llm abstraction
    try:
        llm = get_llm_abstraction()
    except Exception as e:
        raise Exception(
            f"-- {state.executor_label} | find_x_best_jobs_node() | ERROR : llm is None"
        )

    # get human message
    try:
        human_message = await get_human_message(state.input_data.applicant_description, state.input_jobs, state.input_data.cv, state.input_data.X)
    except Exception as e:
        raise Exception(
            f"-- {state.executor_label} | find_x_best_jobs_node() | ERROR building human message: {e}"
        )

    # call llm
    try:
        response = await llm.with_structured_output(
            FindXBestJobsModel, include_raw=True
        ).ainvoke([human_message])
    except Exception as e:
        raise Exception(
            f"-- {state.executor_label} | find_x_best_jobs_node() | ERROR calling llm: {e}"
        )

    # update graph state (see doc of LangGraph how to correctly update the state of a graph !)
    return {
        "x_best_jobs": response["parsed"].x_best_jobs,
    }
