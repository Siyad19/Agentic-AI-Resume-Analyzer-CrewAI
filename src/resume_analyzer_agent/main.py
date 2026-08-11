import sys
import warnings

from datetime import datetime

from src.resume_analyzer_agent.crew import ResumeAnalyzerAgent

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


# def run(resume_path, target_role=None, job_description=None):
#     """
#     Run the crew.
#     """
#     inputs = { 
#         # 'resume': "resumes/sample_resume.pdf",
#         'resume_path': resume_path, 
#         'target_role': target_role,
#         'job_description': job_description,
#         'current_year': str(datetime.now().year)
#     }

#     result = ResumeAnalyzerAgent().crew().kickoff(inputs=inputs)

#     return result

def analyze_resume(resume_path, target_role):

    """Analyze the resume and provide insights based on the target role."""

    inputs = {
        'resume_path': resume_path, 
        'target_role': target_role,
        'current_year': str(datetime.now().year)
    }

    return ResumeAnalyzerAgent().resume_analyzer_crew().kickoff(
        inputs=inputs
    )

def compare_resume_job_description(resume_path, job_description):
    """Compare the resume and Job description provide insights"""

    inputs = {
        'resume_path': resume_path,
        'job_description': job_description,
    }

    return ResumeAnalyzerAgent().compare_resume_with_job_desc_crew().kickoff(
            inputs=inputs
        )

    # try:
    #     ResumeAnalyzerAgent().crew().kickoff(inputs=inputs)
    # except Exception as e:
    #     raise Exception(f"An error occurred while running the crew: {e}")


# def train():
#     """
#     Train the crew for a given number of iterations.
#     """
#     inputs = {
#         'resume': "resumes/sample_resume.pdf",
#         'current_year': str(datetime.now().year)
#     }
#     try:
#         ResumeAnalyzerAgent().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

#     except Exception as e:
#         raise Exception(f"An error occurred while training the crew: {e}")

# def replay():
#     """
#     Replay the crew execution from a specific task.
#     """
#     try:
#         ResumeAnalyzerAgent().crew().replay(task_id=sys.argv[1])

#     except Exception as e:
#         raise Exception(f"An error occurred while replaying the crew: {e}")

# def test():
#     """
#     Test the crew execution and returns the results.
#     """
#     inputs = {
#         'resume': "resumes/sample_resume.pdf",
#         'current_year': str(datetime.now().year)
#     }

#     try:
#         ResumeAnalyzerAgent().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

#     except Exception as e:
#         raise Exception(f"An error occurred while testing the crew: {e}")

# def run_with_trigger():
#     """
#     Run the crew with trigger payload.
#     """
#     import json

#     if len(sys.argv) < 2:
#         raise Exception("No trigger payload provided. Please provide JSON payload as argument.")

#     try:
#         trigger_payload = json.loads(sys.argv[1])
#     except json.JSONDecodeError:
#         raise Exception("Invalid JSON payload provided as argument")

#     inputs = {
#         "crewai_trigger_payload": trigger_payload,
#         "resume": "resumes/sample_resume.pdf",
#         "current_year": str(datetime.now().year)
#     }

#     try:
#         result = ResumeAnalyzerAgent().crew().kickoff(inputs=inputs)
#         return result
#     except Exception as e:
#         raise Exception(f"An error occurred while running the crew with trigger: {e}")
