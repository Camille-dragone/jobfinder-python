from jobfinder_python.logging.logging import app_logger
from langgraph.graph import StateGraph, END
from jobfinder_python.ai.graphs.find_X_best_jobs_graph.states import FindXBestJobsGraphState
from jobfinder_python.ai.graphs.find_X_best_jobs_graph.nodes.find_x_best_jobs_node import find_x_best_jobs_node


def find_x_best_jobs_graph():
    app_logger.info("-- find_x_best_jobs_graph()")

    workflow = StateGraph(FindXBestJobsGraphState)
    workflow.add_node("find_x_best_jobs_node", find_x_best_jobs_node)
    workflow.set_entry_point("find_x_best_jobs_node")
    workflow.add_edge("find_x_best_jobs_node", END)
    graph = workflow.compile()
    return graph


def get_find_x_best_jobs_graph():
    app_logger.info("-- get_find_x_best_jobs_graph()")

    global find_x_best_jobs_graph_object
    if "find_x_best_jobs_graph_object" not in globals():
        find_x_best_jobs_graph_object = find_x_best_jobs_graph()
    return find_x_best_jobs_graph_object  # type: ignore
