import urllib
import json

def printTweets(results):
  for tweet in results:
    print tweet['text']

def getPageofTweets(subject = '', pagenumber = 0):
  response = urllib.urlopen("http://search.twitter.com/search.json?q=%s&page=%i" % (subject, pagenumber))
  return json.load(response)['results']


for x in range(1,10):
  printTweets(getPageofTweets('microsoft', x))