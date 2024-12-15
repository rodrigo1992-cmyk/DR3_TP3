from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper
from langchain.agents import Tool

def instance_lang_chain_tools():
    '''
    Function initializes and returns a list of tools designed for information retrieval.
    '''
    
    wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
    search = DuckDuckGoSearchAPIWrapper()
    
    tools = [
        Tool(
            name="Wikipedia",
            func=wikipedia.run,
            description="Use for fetch general informations and artist history from Wikipedia."
        ),
        Tool(
            name="Internet Search",
            func=search.run,
            description="Use for search current information and news, such as recent releases and tour schedules."
        )
    ]

    return tools