import os
import requests

def scrape_linkedin_profile(linkedin_profile_url: str):
    """Scrape a LinkedIn profiles,
    Manually scrape the information from LinkedIn profile"""
    #api_endpoint = 'https://gist.githubusercontent.com/MarkiyanPyts/d856d6116cec2755f8ff9bf26552cd98/raw/886379f0192eea16985df54fa711e1b69b69a720/mark.json'
    print(f"I got this linkedin profile url: {linkedin_profile_url}")
    response = requests.get("https://gist.githubusercontent.com/MarkiyanPyts/d856d6116cec2755f8ff9bf26552cd98/raw/886379f0192eea16985df54fa711e1b69b69a720/mark.json")

    if response.status_code == 200:
        data = response.json()
    
        data = {
            k: v
            for k, v in data.items()
            if v not in ([], "", "", "None")
            and k not in ["people_also_viewed", "certifications"]
        }
        if data.get("groups"):
            for group_dict in data.get("groups"):
                group_dict.pop("profile_pic_url")

        return data
    else:
        return None