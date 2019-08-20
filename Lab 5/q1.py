from pprint import pprint

def getFreqTable(arr = []):
    counted = []
    freqTable = {}
    for ele in arr:
        if (ele not in counted):
            counted.append(ele)
            freq = neighbours.count(ele)
            freqTable[ele]  = freq
    return freqTable

# print("Calculating Predictions 🤔")

wordNeighbours = {}
with open("data.txt") as fp:
    for i, line in enumerate(fp):
        words = line.split(" ")
        for n in range(1, 6):
            for index in range(0, len(words)-n):
                combinedWordCurrent = (' '.join(words [index : index + n])).replace("\n", '').lower()
                wordNext = (words[index + n]).replace("\n", '').lower()
                if((combinedWordCurrent in wordNeighbours.keys()) == False):
                    wordNeighbours[combinedWordCurrent] = []
                wordNeighbours[combinedWordCurrent].append(wordNext)

wordNeighbourFreqency = {}
for word, neighbours in wordNeighbours.items():
    wordNeighbourFreqency[word] = getFreqTable(neighbours)

# pprint(wordNeighbours)
# pprint(wordNeighbourFreqency)

def predict(word  = "I"):
    if(word in wordNeighbourFreqency.keys()):
        ranking = sorted(wordNeighbourFreqency[word].items(), key = lambda x : x[1])[::-1]
        predictions = []
        for word, rank in ranking:
            predictions.append(word)
        return predictions
    else:
        return ['i']

inp = str(input("Enter String : ")).lower()
while(inp !="exit"):

    predictions = predict(inp)


    for index in range(len(predictions)):
        print(f"{index+1}) {inp} {predictions[index]}")

    randomSentence = [inp]
    for num in range(0,4):
        randomSentence.append( predict( randomSentence[len(randomSentence) - 1] )[0] )
    print('Sentence : ' + ' '.join(randomSentence) + ".")

    inp = str(input("Enter String : ")).lower()
