import requests

#Make an API call and check the response
url="https://api.github.com/search/repositories?q=language:python+sort:stars+stars:>10000"
header={"Accept":"application/vnd.github.v3+json"}
r=requests.get(url,headers=header)
print(f"Status code: {r.status_code}")

#Convert the response object to a dictionary
response_dict=r.json()

#Process results
print(response_dict.keys())