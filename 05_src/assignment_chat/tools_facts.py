from langchain.tools import tool
import json
import requests


@tool
def get_fun_fact():
    """
    Returns a random fun fact from Useless Facts API
    """
    url = "https://uselessfacts.jsph.pl/api/v2/facts/random"
    response = requests.get(url)
    resp_dict = json.loads(response.text)
    resp_text = resp_dict.get("text")
    fact = f"Did you know: {resp_text}"
    return fact
