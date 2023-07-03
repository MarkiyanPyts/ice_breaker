from langchain.serpapi import SerpAPIWrapper

def get_profile_url(text: str) -> str:
    """Search for linkedin Profile Page Url"""
    search = SerpAPIWrapper()
    res = search.run(f"{text}")
    return res
   