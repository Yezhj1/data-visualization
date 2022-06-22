from urllib import response
import requests

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers)
print(f"Status code: {r.status_code}")

response_dict = r.json()
print(f"totle respositories: {response_dict['totle_count']}")

repo_dicts = response_dict['items']


print(response_dict.keys())