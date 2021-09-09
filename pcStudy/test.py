import requests

url1 = "http://shuyantech.com/api/cndbpedia/ment2ent?q=王一博"
url2 = "http://shuyantech.com/api/cndbpedia/avpair?q=王一博"
response = requests.get(url2)
print(response.status_code)
print(response.text)
