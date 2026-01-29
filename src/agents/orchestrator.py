from typing import List, Dict, Any
# from langchain.agents import AgentExecutor # Removed
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from src.agents.email_agent import create_email_agent
from src.agents.calendar_agent import create_calendar_agent
from src.agents.task_agent import create_task_agent
from src.utils.config import settings
import logging

logger = logging.getLogger(__name__)

class MasterOrchestrator:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=settings.GEMINI_API_KEY)
        self.email_agent = create_email_agent()
        self.calendar_agent = create_calendar_agent()
        self.task_agent = create_task_agent()

    def route_request(self, user_input: str) -> str:
        """
        Analyzes the user input and routes it to the appropriate sub-agent.
        """
        prompt = PromptTemplate.from_template(
            """You are a Master Orchestrator for a personal automation system.
            You have three specialized agents:
            1. Email Agent: Reads and summarizes emails.
            2. Calendar Agent: Manages calendar events (check, create, update).
            3. Task Agent: Manages tasks in Notion (create, list, update).

            Analyze the user's request and decide which agent should handle it.
            Return one of the following words: "EMAIL", "CALENDAR", "TASK", or "GENERAL" if it doesn't fit specific agents.
            
            User Request: {input}
            Decision:"""
        )
        
        chain = prompt | self.llm
        decision = chain.invoke({"input": user_input}).content.strip().upper()
        
        logger.info(f"Routing decision: {decision}")
        
        if "EMAIL" in decision:
            return self.email_agent.invoke({"input": user_input})['output']
        elif "CALENDAR" in decision:
            return self.calendar_agent.invoke({"input": user_input})['output']
        elif "TASK" in decision:
            return self.task_agent.invoke({"input": user_input})['output']
        else:
            return "I am not sure how to handle this request directly. Please be more specific about using Email, Calendar, or Tasks."

    def run_workflow(self, workflow_type: str, context: Dict[str, Any] = None):
        """
        Executes predefined multi-step workflows.
        """
        if workflow_type == "daily_summary":
            return self._run_daily_summary()
        # Add more workflows here
        return "Unknown workflow type."

    def _run_daily_summary(self):
        # 1. Get calendar events for today
        events = self.calendar_agent.invoke({"input": "What are my events for today?"})['output']
        
        # 2. Get high priority tasks
        tasks = self.task_agent.invoke({"input": "List my high priority tasks."})['output']
        
        # 3. Get unread emails (limit to top 3)
        emails = self.email_agent.invoke({"input": "Summarize my top 3 unread emails."})['output']
        
        # 4. Synthesize summary
        summary_prompt = f"""
        Here is the data for today's summary:
        
        Calendar: {events}
        Tasks: {tasks}
        Emails: {emails}
        
        Please provide a concise and encouraging daily briefing for the user.
        """
        summary = self.llm.invoke(summary_prompt).content
        return summary
