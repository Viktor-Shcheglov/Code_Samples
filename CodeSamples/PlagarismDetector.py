def CreateSynonymsDictionary(inputs):
	"""
	Will go through the input string spliting it by | and then by white spaces. After that will create a dictionary of all words that are not the first word as keys
	and set the values of the keys to be the first word. This is done to be able to replace all the words with the same meaning as 1 word to be able to identify matching tuples.
	"""
	SynonymsDictionaryt = dict()
	inputs = inputs.split('|')
	for words in inputs:
		tempwords = words.split()
		for wordIndex in range(1,len(tempwords)):
			SynonymsDictionaryt[tempwords[wordIndex]]=tempwords[0]
	return SynonymsDictionaryt

def CreateOriginalSet(inputs,tupleSize,SynonymsDictionary):
	"""
	Will go through the original text spliting all the words and then using the alphabet to remove any remaining punctuation. Assumes that there are no quotes in the text and proper use of white space.
	Creates a set of all possible combination of tupples and return the set.
	"""
	inputs = inputs.split()
	alphabet={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0'}
	OriginalSet = set()
	tempTuple = []
	for word in inputs:
		tempword= word.lower()
		templist = []
		for char in tempword:
			if char in alphabet:
				templist.append(char)
		if len(templist)>0:
			tempword = ''.join(templist)
			if tempword in SynonymsDictionary:
				tempword = SynonymsDictionary[tempword]
			tempTuple.append(tempword)
			if len(tempTuple)==tupleSize:
				OriginalSet.add(tuple(tempTuple))
				tempTuple.pop(0)
	return OriginalSet

def solution(inputs,tupleSize):
	if len(inputs)!= 3:
		print('Inputs array must be of size 3')
	if tupleSize<1:
		print('tupleSize needs to be of size 1 or greater')
		return
	SynonymsDictionary = CreateSynonymsDictionary(inputs[0]) #generates a dictionary for all synonums which will be used to replace every synonum word with 1 word so that tuples match. 
	OriginalSet = CreateOriginalSet(inputs[1],tupleSize,SynonymsDictionary) #generates a set of all possible tupleSize-tuples in the original text.
	"""
	Go thorugh the entire suspect text and generate the tuples. If the tuple matches a tuple in the OriginalSet add 1 to the count of matches. Add 1 for each tupple generated.
	At the end compute the percentage of unique vs repeated tupples and return the value.
	"""
	alphabet = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0'}
	tempTuple = []
	matchedTuples = 0
	totalTuples = 0
	for word in inputs[2].split():
		tempword = word.lower() #two temporary variables to maintain the integrity of the original string
		templist = []
		for char in tempword:
			if char in alphabet:
				templist.append(char)	
		if len(templist)>0:
			tempword = ''.join(templist)
			if tempword in SynonymsDictionary:
				tempword = SynonymsDictionary[tempword]
			tempTuple.append(tempword)
			if len(tempTuple)==tupleSize:
				if tuple(tempTuple) in OriginalSet:
					matchedTuples+=1
				totalTuples+=1
				tempTuple.pop(0)
	#end calculations to make sure return the correct value as described by the question
	if totalTuples == 0:
		print('tupleSize was larger then number of words in suspectText or no valid tuples were created')
		return
	returnValue = (matchedTuples/totalTuples)*100
	if returnValue == int(returnValue):
		print(int(returnValue))
		return
	else:
		print(int(returnValue)+1)
		return

solution(["","go for a jog","go for a run"],3)


