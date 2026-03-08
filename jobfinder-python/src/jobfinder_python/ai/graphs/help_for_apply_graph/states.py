from jobfinder_python.api.api_model import HelpForApplyDto
from jobfinder_python.ai.graphs.help_for_apply_graph.models import HelpForApplyModel
from pydantic import BaseModel
from jobfinder_python.api.api_model import Job

class HelpForApplyGraphState(BaseModel):
    executor_label: str = "help_for_apply_graph"
    # input data
    input_data: HelpForApplyDto | None = None
    help_for_apply: HelpForApplyModel | None = None
