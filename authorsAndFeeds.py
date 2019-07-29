import requests


myUrl = "https://api.rss2json.com/v1/api.json?rss_url=https%3A%2F%2Fwww.theguardian.com%2Fworld%2Frss"


response = requests.get(myUrl)
data = response.json()


authorsAndFeeds = {}


for each in data['items']:
    author = each['author']
    newsFeed = each['description']
    authorsAndFeeds.update({author: newsFeed})


#Output test
print(authorsAndFeeds)
