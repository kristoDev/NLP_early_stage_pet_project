import requests
import re
​
​
myUrl = "https://api.rss2json.com/v1/api.json?rss_url=https%3A%2F%2Fwww.theguardian.com%2Fworld%2Frss"
​
​
response = requests.get(myUrl)
data = response.json()
​
​
authorsAndFeeds = {}
​
​
# to remove html tags
def remove_tags(myString):
    removeHTMLtags = re.compile(r'<[^>]+>')
    return removeHTMLtags.sub('', myString)
​
​
for each in data['items']:
    author = each['author']
    newsFeed = remove_tags(each['description'])
    authorsAndFeeds.update({author: newsFeed})
​
​
# to remove "/n" to each value in our dict!
# the reason why I didn't simply included the strip() 
# trick from my previous loop it because it seems to 
# make the program run significantly slow!!!
for eachKey, eachValue in authorsAndFeeds.items():
    cleanedValue = eachValue.strip("\n")
    authorsAndFeeds[eachKey] = cleanedValue
​
​
# test output
print(authorsAndFeeds)
