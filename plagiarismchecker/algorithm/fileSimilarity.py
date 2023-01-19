import re
import math
from nltk.corpus import stopwords


def findFileSimilarity(inputQuery, database):

	universalSetOfUniqueWords = []
	matchPercentage = 0

	lowercaseQuery = inputQuery.lower()
	en_stops = set(stopwords.words('english'))

	# Replace punctuation by space and split
	queryWordList = re.sub("[^\w]", " ", lowercaseQuery).split()
	# queryWordList = map(str, queryWordList)					#This was causing divide by zero error

	for word in queryWordList:
		if word not in universalSetOfUniqueWords:
			universalSetOfUniqueWords.append(word)

	database1 = database.lower()

	# Replace punctuation by space and split
	databaseWordList = re.sub("[^\w]", " ", database1).split()
	# databaseWordList = map(str, databaseWordList)			#And this also leads to divide by zero error

	for word in databaseWordList:
		if word not in universalSetOfUniqueWords:
			universalSetOfUniqueWords.append(word)

	for word in universalSetOfUniqueWords:
		if word in en_stops:
			universalSetOfUniqueWords.remove(word)

	queryTF = []
	databaseTF = []

	for word in universalSetOfUniqueWords:
		queryTfCounter = 0
		databaseTfCounter = 0

		for word2 in queryWordList:
			if word == word2:
				queryTfCounter += 1
		queryTF.append(queryTfCounter)

		for word2 in databaseWordList:
			if word == word2:
				databaseTfCounter += 1
		databaseTF.append(databaseTfCounter)

	dotProduct = 0
	for i in range(len(queryTF)):
		dotProduct += queryTF[i]*databaseTF[i]

	queryVectorMagnitude = 0
	for i in range(len(queryTF)):
		queryVectorMagnitude += queryTF[i]**2
	queryVectorMagnitude = math.sqrt(queryVectorMagnitude)

	databaseVectorMagnitude = 0
	for i in range(len(databaseTF)):
		databaseVectorMagnitude += databaseTF[i]**2
	databaseVectorMagnitude = math.sqrt(databaseVectorMagnitude)

	matchPercentage = (float)(
		dotProduct / (queryVectorMagnitude * databaseVectorMagnitude))*100

# 	print (universalSetOfUniqueWords)
# 	print()
# 	print (databaseWordList)


# 	print (queryTF)
# 	print (databaseTF)

	return matchPercentage
