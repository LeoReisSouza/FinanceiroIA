from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import tool
from langchain_community.utilities import GoogleSerperAPIWrapper
from dotenv import load_dotenv
import os

load_dotenv()

class FinancialAgent:
    def __init__(self):
        self.llm = ChatOpenAI(
            temperature=0,
            model="openai/gpt-3.5-turbo", 
            openai_api_key=os.getenv("OPENROUTER_API_KEY"),
            base_url="https://openrouter.ai/api/v1"
        )
        self.tools = self._setup_tools()
        self.agent = self._create_agent()
    
    def _setup_tools(self):
        @tool
        def pesquisa(query: str) -> str:
            """Pesquisa informações financeiras atuais"""
            try:
                search = GoogleSerperAPIWrapper()
                return search.run(query)
            except Exception as e:
                return f"Erro na pesquisa: {str(e)}"
        
        return [pesquisa]
    
    def _create_agent(self):
        prompt = ChatPromptTemplate.from_messages([
            ("system", "Você é um especialista em finanças."),
            ("human", "{input}"),
            MessagesPlaceholder("agent_scratchpad")
        ])
        
        agent = create_tool_calling_agent(self.llm, self.tools, prompt)
        return AgentExecutor(agent=agent, tools=self.tools)
    
    def query(self, question: str) -> str:
        try:
            response = self.agent.invoke({"input": question})
            return response["output"]
        except Exception as e:
            return f"Erro: {str(e)}"
