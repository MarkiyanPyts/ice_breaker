from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool, AgentType

from tools.tools import get_profile_url


def lookup(name: str) -> str:
    """Lookup a LinkedIn profile by name."""
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    template = """
        given the full name {name_of_person} I want you to get me a link to their Linkedin profile page
        your answer should only contain a URL
    """

    
    tools_for_agent = [Tool("Crawl Google for linkedin profile page", func=get_profile_url, description="useful for when you need to get Linkedin Page URL")]

    agent = initialize_agent(tools=tools_for_agent, agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION, llm=llm, verbose=True,)
    prompt_template = PromptTemplate(template=template, input_variables=["name_of_person"])

    linked_profile_url = agent.run(prompt_template.format_prompt(name_of_person=name))

    return linked_profile_url