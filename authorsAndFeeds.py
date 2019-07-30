
import requests
from bs4 import BeautifulSoup




myUrl = "https://api.rss2json.com/v1/api.json?rss_url=https%3A%2F%2Fwww.theguardian.com%2Fworld%2Frss"


response = requests.get(myUrl)
data = response.json()


authorsAndFeeds = {}



for each in data['items']:
    author = each['author']
    newsFeed = each['description']
    authorsAndFeeds.update({author: newsFeed})

    

# now removing html tags to each news feed
for eachKey, eachValue in authorsAndFeeds.items():
    valueToClean = BeautifulSoup(eachValue,'lxml')

    stored_sentences =[]

    for each_p in valueToClean.find_all('p'):
        stored_sentences.append(each_p.string)
        authorsAndFeeds[eachKey] = stored_sentences


        
#test output 
print(authorsAndFeeds)
