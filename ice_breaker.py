from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

from third_parties.linkedin import scrape_linkedin_profile

import os

if __name__ == '__main__':

    summary_template = '''
        given the Linkedin information {information} about a person from I want you to create
        1. A Short Summary
        2. Two Interesting facts about them
    '''

    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    linkedin_data = scrape_linkedin_profile('https://gist.githubusercontent.com/MarkiyanPyts/d856d6116cec2755f8ff9bf26552cd98/raw/886379f0192eea16985df54fa711e1b69b69a720/mark.json')

    print(chain.run(information=linkedin_data))
    