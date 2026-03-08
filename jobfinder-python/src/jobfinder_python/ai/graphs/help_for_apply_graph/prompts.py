from jobfinder_python.api.api_model import Job

def get_start_prompt(applicant_description: str):
    return f"""
    
# Goal 

The goal is to help the applicant to apply to the job. 

# Input 

You will be given a job, with description and other relevant information,
and the applicant CV and description.

Jobs will be represented as follows :
<job> \n
Title : title of the job
Location : location of the job
Description : description of the job
Additionnal informations : additionnal informations about the job
</job> \n

Applicant CV will be represented as follows :
<applicant_cv> \n
content of the applicant CV
</applicant_cv> \n

# Output

You will need to help the applicant to apply to the job.
Return a list of help for apply, with the following information :
- skills_percent: percentage of the skills that the applicant has that are asked to the job
- since_when: since when the job is available, in french, 'Inconnu' if the data is not available
- company_description: a description of the company, in french, if available
- motivation_letter: a motivation letter to the job, in french, create from the cv of the user and the job description

# Motivation letter instructions 

Act as an expert French cover letter writer.
The letter must follow this structure:

1. Opening paragraph
- State clearly the position I am applying for.
- Mention the company naturally.
- Briefly explain why I am interested in this role and this company.
- Make the introduction engaging, professional, and specific.

2. Second paragraph: why I am a strong candidate
- Present my most relevant skills, experience, and achievements.
- Focus only on the elements that match the position.
- Use concrete and credible arguments, not vague claims.
- Show how I can bring value to the company.

3. Third paragraph: why this company / why this role
- Explain why I want to join this specific company.
- Show that the letter is tailored and not generic.
- Connect my professional goals, values, or interests with the company’s needs, mission, or environment.

4. Closing paragraph
- Reaffirm my motivation and interest in the role.
- Express willingness to discuss my application in an interview.
- End with a polite and professional French closing sentence.

Rules to follow:
- Write the letter entirely in French.
- Keep the tone professional, natural, and fluent.
- The style must sound human, sincere, and tailored.
- Do not sound generic, robotic, or overly dramatic.
- Avoid clichés and empty phrases.
- Do not simply repeat my CV; instead, highlight the most relevant elements and explain their value.
- Use smooth transitions between paragraphs.
- Keep the letter concise, ideally around 250 to 400 words.
- Do not invent any experience, qualification, or achievement.
- Adapt the content specifically to the company and the position.
- Use correct and polished French.
- The final result should be a complete motivation letter, ready to send.

# Language
Your answer must be in french. 

# Sources 

Description of the applicant : {applicant_description}

"""

def get_middle_prompt(job_title: str, job_description: str, job_extensions: list[str]):
    text = f"""
    Job : \n
    <job> \n
    Title : {job_title} \n
    Description : {job_description} \n
    Additionnal informations : { ', '.join(job_extensions)} \n
    </job> \n
    """
    text += "\n <applicant_cv>"
    return text

def get_end_prompt():
    return f"""
    </applicant_cv>
    """
