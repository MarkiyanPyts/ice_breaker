from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from third_parties.linkedin import scrape_linkedin_profile

import os

if __name__ == '__main__':

    linkedin_profile_url = linkedin_lookup_agent(name="Pyts Markiyan")
    print(f"starting search for {linkedin_profile_url}")

    summary_template = '''
        given the Linkedin information {information} about a person from I want you to create
        1. A Short Summary
        2. Two Interesting facts about them
    '''

    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    linkedin_data = scrape_linkedin_profile(linkedin_profile_url)

    print(chain.run(information=linkedin_data))
    