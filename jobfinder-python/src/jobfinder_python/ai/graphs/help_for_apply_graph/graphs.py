from jobfinder_python.logging.logging import app_logger
from langgraph.graph import StateGraph, END
from jobfinder_python.ai.graphs.help_for_apply_graph.states import HelpForApplyGraphState
from jobfinder_python.ai.graphs.help_for_apply_graph.nodes.help_for_apply_node import help_for_apply_node


def help_for_apply_graph():
    app_logger.info("-- help_for_apply_graph()")

    workflow = StateGraph(HelpForApplyGraphState)
    workflow.add_node("help_for_apply_node", help_for_apply_node)
    workflow.set_entry_point("help_for_apply_node")
    workflow.add_edge("help_for_apply_node", END)
    graph = workflow.compile()
    return graph


def get_help_for_apply_graph():
    app_logger.info("-- get_help_for_apply_graph()")

    global help_for_apply_graph_object
    if "help_for_apply_graph_object" not in globals():
        help_for_apply_graph_object = help_for_apply_graph()
    return help_for_apply_graph_object  # type: ignore
