import pdfplumber
from typing import Type
from crewai.tools import BaseTool
from pydantic import BaseModel, Field


class PDFParserInput(BaseModel):
    resume: str = Field(
        ...,
        description="The exact local file path of the PDF resume to parse."
    )


class PDFParserTool(BaseTool):
    name: str = "pdf_resume_parser"
    description: str = (
        "Extract text from a resume PDF file. "
        "IMPORTANT: The 'resume' argument must ALWAYS be the local file path "
        "to the PDF, such as 'resumes/Siyad-Resume.pdf'. "
        "Do NOT pass resume text, resume content, or extracted resume information "
        "as the 'resume' argument."
    )

    args_schema: Type[BaseModel] = PDFParserInput

    def _run(self, resume: str) -> str:
        text = ""

        with pdfplumber.open(resume) as pdf:
            for page in pdf.pages:
                extracted = page.extract_text()

                if extracted:
                    text += extracted + "\n"

        return text.strip()