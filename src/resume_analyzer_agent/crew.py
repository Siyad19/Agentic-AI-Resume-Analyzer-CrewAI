from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import SerperDevTool
from src.resume_analyzer_agent.tools.pdf_parser import PDFParserTool
import crewai.llms.cache as crewai_cache

crewai_cache.mark_cache_breakpoint = lambda msg: msg

import os
from dotenv import load_dotenv

load_dotenv()

@CrewBase
class ResumeAnalyzerAgent():
    """ResumeAnalyzerAgent crew"""

    agents: list[BaseAgent]
    tasks: list[Task]

    def __init__(self):
        # self.llm = LLM(
        #     model="groq/llama-3.1-8b-instant", 
        #     temperature=0.2,
        #     api_key=os.getenv("GROQ_API_KEY"),
        #     max_tokens=1500
        self.llm = LLM(
        model="openrouter/meta-llama/llama-4-maverick",
        temperature=0.2,
        api_key=os.getenv("OPENROUTER_API_KEY")
    )

    @agent
    def resume_analyzer(self) -> Agent:
        return Agent(
            llm=self.llm,
            config=self.agents_config['resume_analyzer'], # type: ignore[index]
            verbose=True,
            tools=[PDFParserTool()]
        )

    @agent
    def career_advisor(self) -> Agent:
        return Agent(
            llm=self.llm,
            config=self.agents_config['career_advisor'], # type: ignore[index]
            verbose=True,
            tools=[SerperDevTool()]
        )

    @agent
    def job_description_analyzer(self) -> Agent:
        return Agent(
            llm=self.llm,  
            config=self.agents_config['job_description_analyzer'], # type: ignore[index]
            verbose=True
        )

    @agent
    def keyword_gap_analyzer(self) -> Agent:
        return Agent(
            llm=self.llm,
            config=self.agents_config['keyword_gap_analyzer'], # type: ignore[index]
            verbose=True
        )

    @task
    def analyzer_task(self) -> Task:
        return Task(
            config=self.tasks_config['analyzer_task'], # type: ignore[index]
        )

    @task
    def advisor_task(self) -> Task:
        return Task(
            config=self.tasks_config['advisor_task'], # type: ignore[index]
            output_file='career_plan.md'
        )

    @task
    def job_description_task(self) -> Task:
        return Task(
            config=self.tasks_config['job_description_task'], # type: ignore[index]
        )

    @task
    def keyword_gap_task(self) -> Task:
        return Task(
            config=self.tasks_config['keyword_gap_task'], # type: ignore[index]
        )

 
    @crew
    def resume_analyzer_crew(self) -> Crew:
        """Creates the ResumeAnalyzerAgent crew"""
        return Crew(
            agents=[self.resume_analyzer(), self.career_advisor()],
            tasks=[self.analyzer_task(), self.advisor_task()],
            process=Process.sequential,
            verbose=True,
        )

    @crew
    def compare_resume_with_job_desc_crew(self) -> Crew:
        """Creates the ResumeAnalyzerAgent crew for comparing resume with job description"""
        return Crew(
            agents=[self.job_description_analyzer(), self.keyword_gap_analyzer()],
            tasks=[self.job_description_task(), self.keyword_gap_task()],
            process=Process.sequential,
            verbose=True,
        )