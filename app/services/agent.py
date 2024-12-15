from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import AgentExecutor, create_react_agent
from langchain import hub
from langchain.memory import ConversationBufferMemory
from langchain.agents import AgentType
from dotenv import load_dotenv
import os
from tools import instance_lang_chain_tools


load_dotenv()

if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = os.getenv('GOOGLE_API_KEY')

if "GOOGLE_CSE_ID" not in os.environ:
    os.environ["GOOGLE_CSE_ID"] = os.getenv('GOOGLE_CSE_ID')

memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True,
    verbose=True,
)

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.7
)


def invoke_agent():
    '''
    This function creates an agent that can be used to interact with the user.

    Returns:
    agent_executor: AgentExecutor
    '''
    tools = instance_lang_chain_tools()

    agent_prompt = hub.pull("musicindustrysearch/prompt")
    agent = create_react_agent(llm, tools, agent_prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, memory=memory, max_turns=3)
    
    return agent_executor

def ask_to_lmm(user_input):
    '''
    This function invoke the agent passing the question on user input.
    
    Args:
    user_input: str
    '''

    agent = invoke_agent()
    response = agent({"input": user_input})
    return response 