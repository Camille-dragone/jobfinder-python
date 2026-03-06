from jobfinder_python.api.api_model import Job

def get_start_prompt(description: str, X: int):
    return f"""
    
# Goal 

The goal is to extract the {X} best jobs from the list of jobs. 

# Input 

You will be given a list of jobs, with description and other relevant information,
and the applicant CV and description.

Jobs will be represented as follows :
"<job> \n
UUID : uuid of the job 
Company : company name
Job : job title
Description : job description
Additionnal informations : additionnal informations about the job
</job> \n

Applicant CV will be represented as follows :
<applicant_cv> \n
content of the applicant CV
</applicant_cv> \n

# Output

You will need to extract the X best jobs from the list of jobs.
Take care that the job are relevant to the applicant level and experience.
Sort the jobs by relevance and return the X best jobs.

# Language
Your answer must be in french.

# Sources 

Description of the applicant : {description}

"""

def get_middle_prompt(jobs: list[Job]):
    text = "List of jobs : \n"
    for job in jobs:
        text += f"""
        <job> \n
        UUID : {job.uuid} \n
        Company : {job.company} \n
        Job : {job.title} \n
        Description : {job.description} \n
        Additionnal informations : { ', '.join(job.extensions)} \n
        </job> \n
    """
    text += "\n <applicant_cv>"
    return text

def get_end_prompt():
    return f"""
    </applicant_cv>
    """
