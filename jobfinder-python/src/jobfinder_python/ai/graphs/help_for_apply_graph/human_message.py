from jobfinder_python.ai.graphs.help_for_apply_graph.models import HelpForApplyModel
from langchain_core.messages import HumanMessage
from jobfinder_python.ai.graphs.help_for_apply_graph.prompts import get_start_prompt, get_middle_prompt, get_end_prompt
from fastapi import UploadFile
from pypdf import PdfReader
from docx import Document
from io import BytesIO
from jobfinder_python.api.api_model import HelpForApplyDto

async def get_human_message(input_data: HelpForApplyDto):
    human_message_content = []

    # build prompt
    prompt = get_start_prompt(input_data.applicant_description)
    prompt += get_middle_prompt(input_data.job_title, input_data.job_description, input_data.job_extensions)
    # add applicant CV
    prompt += await extract_cv_text(input_data.cv)
    prompt += get_end_prompt()
    human_message_content.append(prompt)

    # build human message from prompt
    human_message = HumanMessage(
        content="\n".join(human_message_content)
    )
    return human_message

async def extract_cv_text(cv: UploadFile) -> str:
    try: 
        await cv.seek(0) # reset cursor to the beginning of the file
        raw = await cv.read()
        content_type = (cv.content_type or "").lower()

        if content_type == "text/plain":
            text = raw.decode("utf-8", errors="ignore")

        elif content_type == "application/pdf":
            reader = PdfReader(BytesIO(raw))
            text = "\n".join((p.extract_text() or "") for p in reader.pages)

        elif content_type in {
            "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            "application/msword",
        }:
            doc = Document(BytesIO(raw))
            text = "\n".join(p.text for p in doc.paragraphs)
        else:
            raise ValueError(f"Unsupported CV format: {cv.content_type}")

        await cv.seek(0)  

        text = " ".join(text.split())  
        return text
    except Exception as e:
        return "Error during extraction of CV, no data for CV"