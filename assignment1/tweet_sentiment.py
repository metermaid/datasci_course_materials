import sys
import json
import re

if len(sys.argv) >= 2:
	sent_file = sys.argv[1]
	tweet_file = sys.argv[2]
else:
	sent_file = "AFINN-111.txt"
	tweet_file = "output.txt"

def readSentiment(sentFile):
	''' reads sentiment file and returns a dict with {word:value}  '''
	afinnfile = open(sentFile)
	scores = {} # initialize an empty dictionary
	for line in afinnfile:
		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
		scores[term] = float(score)  # Convert the score to an float.
	afinnfile.close()

	return scores

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

def scoreTweets(tweetList, scores):
	''' prints out score for each tweet in a list of strings '''
	for tweet in tweetList:
		words = re.split('\W+', tweet)
		score = 0
		for word in words:
			score += scores.get(word, 0)
		print score

def main():
    sentDict = readSentiment(sent_file)
    tweetList = readTweets(tweet_file)

    scoreTweets(tweetList, sentDict)

if __name__ == '__main__':
    main()
