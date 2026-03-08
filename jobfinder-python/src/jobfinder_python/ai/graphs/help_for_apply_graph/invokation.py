import uuid
from jobfinder_python.ai.graphs.help_for_apply_graph.graphs import get_help_for_apply_graph
from jobfinder_python.ai.graphs.help_for_apply_graph.states import HelpForApplyGraphState
from jobfinder_python.api.api_model import HelpForApplyDto


async def invoke_help_for_apply_graph(input_data: HelpForApplyDto):
    # init input state
    input_state = HelpForApplyGraphState(execution_id=str(uuid.uuid4()), input_data=input_data)
    # invoke graph and wait for result
    res = await get_help_for_apply_graph().ainvoke(input=input_state)
    # parse response
    return HelpForApplyGraphState(**res)
