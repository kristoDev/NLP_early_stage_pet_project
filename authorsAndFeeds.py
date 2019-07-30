myUrl = "https://api.rss2json.com/v1/api.json?rss_url=https%3A%2F%2Fwww.theguardian.com%2Fworld%2Frss"


response = requests.get(myUrl)
data = response.json()


authorsAndFeeds = {}


# to remove html tags
def removeTags(here):
    for each_p in here.find_all('p'):
        return each_p.string


for each in data['items']:
    author = each['author']
    newsFeed = each['description']
    authorsAndFeeds.update({author: newsFeed})


#removing html tags within our dict
for eachKey, eachValue in authorsAndFeeds.items():

    cleanedValue = removeTags(
        BeautifulSoup(eachValue,'lxml')
        )
        
    authorsAndFeeds[eachKey] = cleanedValue



print(authorsAndFeeds)
