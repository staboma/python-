import requests
from bs4 import BeautifulSoup as bs

github_profile = "https://github.com/staboma"

try:
    req = requests.get(github_profile)
    req.raise_for_status()  # Raise an exception for non-200 status codes

    scraper = bs(req.content, "html.parser")

    # Improved selector (find image within a specific container)
    profile_container = scraper.find("div", {"class": "clearfix"}).find("img")
    profile_picture = profile_container.get("src") if profile_container else None

    if profile_picture:
        print(profile_picture)
    else:
        print("Profile picture not found using the provided selector.")
except requests.exceptions.RequestException as e:
    print(f"Error retrieving profile: {e}")
except AttributeError:
    print("Profile picture element not found or doesn't have a 'src' attribute.")
