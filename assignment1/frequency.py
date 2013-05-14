import sys
import json
import re

if len(sys.argv) >= 2:
	tweet_file = sys.argv[1]
else:
	tweet_file = "output.txt"

def readTweets(tweetFile):
	''' returns a list of strings (the text from the tweets) '''
	tweets = []
	tweetData = open(tweetFile)
	scores = {} # initialize an empty dictionary
	for line in tweetData:
		tweetText = json.loads(line)
		if tweetText.get("text"):
			tweets.append(tweetText.get("text"))
	tweetData.close()
	return tweets

def termFreq(tweetList):
	''' prints out term frequency '''
	frequency = {}
	termCount = 0

	for tweet in tweetList:
		words = re.split('\s+', tweet)
		for word in words:
			frequency.setdefault(word,0)
        	frequency[word] += 1
        	termCount += 1

	for term in frequency:
		if term.strip() != "":
			count = frequency[term]
			frequent = float(count)/termCount

			print("%s %f" % (term, frequent))

def main():
    tweetList = readTweets(tweet_file)

    termFreq(tweetList)

if __name__ == '__main__':
    main()
