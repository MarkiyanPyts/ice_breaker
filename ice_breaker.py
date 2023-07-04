from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from third_parties.linkedin import scrape_linkedin_profile

from output_parsers import person_intel_parser

import os

def ice_break(name: str) -> str:
    linkedin_profile_url = linkedin_lookup_agent(name=name)
    print(f"starting search for {linkedin_profile_url}")

    summary_template = '''
        given the Linkedin information {information} about a person from I want you to create
        1. A Short Summary
        2. Two Interesting facts about them
        3. A topic that may interest them
        4. 2 creative Ice breakers to open a conversation with them
        \n{format_instructions}
    '''

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
        partial_variables= {
            "format_instructions": person_intel_parser.get_format_instructions()
        }
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    linkedin_data = scrape_linkedin_profile(linkedin_profile_url)

    result = chain.run(information=linkedin_data)

    return person_intel_parser.parse(result)

if __name__ == '__main__':
    ice_break = ice_break(name="Pyts Markiyan")

    print(ice_break)