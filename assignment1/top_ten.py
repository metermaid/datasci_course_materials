import sys
import json
import operator

if len(sys.argv) >= 2:
	tweet_file = sys.argv[1]
else:
	tweet_file = "output.txt"

def readTweets(tweetFile):
	''' returns a list of lists of tweet hashtags '''
	tags = []
	tweetData = open(tweetFile)
	scores = {} # initialize an empty dictionary
	for line in tweetData:
		tweetJSON = json.loads(line)
		if tweetJSON.get("entities"):
			if tweetJSON.get("entities").get("hashtags"):
				tags = tags + tweetJSON.get("entities").get("hashtags")
	tweetData.close()
	return tags

def topTen(tags):
	''' returns top ten tags when given a list of tags '''
	frequency = {}
	for tag in tags:
		frequency.setdefault(tag["text"], 0)
		frequency[tag["text"]] += 1

	topTags = dict(sorted(frequency.iteritems(), key=operator.itemgetter(1), reverse=True)[:10])

	for tag in topTags:
		print "%s %i" % (tag, topTags[tag])

def main():
    tags = readTweets(tweet_file)

    topTen(tags)

if __name__ == '__main__':
    main()
