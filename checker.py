import requests

def check_website_text(url, text):
    """
    Returns True if the provided text is found in the HTML of the webpage 
    """
    resp = requests.get(url)
    return text in resp.text 

