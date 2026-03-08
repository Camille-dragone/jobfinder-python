from pydantic import BaseModel, Field

# ---------------------------------------------------------------
# GRAPH MODEL
# ---------------------------------------------------------------
class HelpForApplyModel(BaseModel):
    skills_percent: int = Field(description="Percentage of the skills that the applicant has that are asked to the job")
    since_when: str = Field(description="Since when the job is available, in french,  'Inconnu' if the data is not available")
    company_description: str = Field(description="A description of the company, in french, if available")
    motivation_letter: str = Field(description="A motivation letter to the job, in french, create from the cv of the user and the job description")

