import os
from jobfinder_python.ai.graphs.help_for_apply_graph.states import HelpForApplyGraphState
from jobfinder_python.ai.graphs.help_for_apply_graph.models import HelpForApplyModel
from jobfinder_python.logging.logging import app_logger
from jobfinder_python.ai.graphs.common.ai_utils import get_llm_abstraction
from jobfinder_python.ai.graphs.help_for_apply_graph.human_message import get_human_message


async def help_for_apply_node(state: HelpForApplyGraphState):
    app_logger.info(f"-- {state.executor_label} | help_for_apply_node()")

    # get llm abstraction
    try:
        llm = get_llm_abstraction()
    except Exception as e:
        raise Exception(
            f"-- {state.executor_label} | help_for_apply_node() | ERROR : llm is None"
        )

    # get human message
    try:
        human_message = await get_human_message(state.input_data)
    except Exception as e:
        raise Exception(
            f"-- {state.executor_label} | help_for_apply_node() | ERROR building human message: {e}"
        )

    # call llm
    try:
        response = await llm.with_structured_output(
            HelpForApplyModel, include_raw=True
        ).ainvoke([human_message])
    except Exception as e:
        raise Exception(
            f"-- {state.executor_label} | help_for_apply_node() | ERROR calling llm: {e}"
        )

    # update graph state (see doc of LangGraph how to correctly update the state of a graph !)
    return {
        "help_for_apply": response["parsed"],
    }
