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

def scoreNewWords(tweetList, scores):
	''' based on other sentiment scores, calculates and
		prints out sentiment scores for new words '''
	newScores = {}

	for tweet in tweetList:
		words = re.split('\s+', tweet)
		score = 0
		newTerms = []
		for word in words:
			prevScore = scores.get(word, None)
			if prevScore == None:
				newTerms.append(word)

			score += scores.get(word, 0)

		for word in newTerms:
			newScores.setdefault(word, [])
			newScores[word].append(score)
	
	for score in newScores:
		if score.strip() != "":
			entry = newScores[score]
			avg = reduce(lambda x, y: x + y, entry) / float(len(entry))
		print("%s %s" % (score.encode('utf-8'), str(avg)))

def main():
    sentDict = readSentiment(sent_file)
    tweetList = readTweets(tweet_file)

    scoreNewWords(tweetList, sentDict)

if __name__ == '__main__':
    main()
