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
	''' returns a list of tweet JSONs '''
	tweets = []
	tweetData = open(tweetFile)
	scores = {} # initialize an empty dictionary
	for line in tweetData:
		tweetJSON = json.loads(line)
		tweets.append(tweetJSON)
	tweetData.close()
	return tweets

def happiestState(tweetList, scores):
	''' prints the happiest State?! '''
	states = {}
	for tweet in tweetList:
		place = tweet.get("place", {})
		if place != None and place.get("country_code", "") == "US":

			name = place.get("full_name")
			state = re.split("\W+", name)[-1]

			text = tweet["text"]
			words = re.split('\W+', text)

			score = 0
			for word in words:
				score += scores.get(word, 0)

			states.setdefault(state, [])
			states[state].append(score)

	print max(states, key=states.get)


def main():
    sentDict = readSentiment(sent_file)
    tweetList = readTweets(tweet_file)

    happiestState(tweetList, sentDict)

if __name__ == '__main__':
    main()
