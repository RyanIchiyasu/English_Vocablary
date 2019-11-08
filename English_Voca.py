import json

##################################
######## CLASS
##################################
class English:
    def __init__(self):
        vocabulary = []

    def readFile(self):
        jsonFile = open("English.json", "r")
        jsonData = json.load(jsonFile)
        self.vocabulary = jsonData
        assert len(self.vocabulary) > 0, "JSON File is empty"

    def saveFile(self):
        jsonFile = open("English.json", "w")
        json.dump(self.vocabulary, jsonFile)

##################################
######## FUNCTIONS
##################################
def sortDictionaly(dic):
    #Add "probability" key
    for i in range(len(dic)):
        if dic[i]["Examed"] == 0:
            dic[i]["Probability"] = 0
        else:
            dic[i]["Probability"] = dic[i]["Correct"] / dic[i]["Examed"]
    #Bubble sort
    change = True
    while change:
        change = False
        for i in range(len(dic) - 1):
            if dic[i]["Probability"] > dic[i+1]["Probability"]:
                temp = dic[i]
                dic[i] = dic[i+1]
                dic[i+1] = temp
                change = True

    return dic

def quiz(dic):
    for i in range(len(dic)):
        print("----------------------------------------------------------------------")
        print("Q" + str(i+1) + "    (" + dic[i]["Type"] + ")" +  "\"" + dic[i]["Japanese"] + "\"    Correct answer: " + str('{:.0f}'.format(dic[i]["Probability"]*100)) + "%")
        dic[i]["Examed"] += 1

        userInput = input("Answer?:  ")

        if userInput == "Z":
            break
        elif userInput == dic[i]["English"]:
            print("Correct!")
            dic[i]["Correct"] += 1
        else:
            print("Wrong Answer. The corret answer is \"" + dic[i]["English"] + "\"")
            dic[i]["Wrong"] += 1
            input("Type again:  ")

    #assert 1==0, "Debug: finished questions"
    return dic

def deleteProbability(dic):
    for i in range(len(dic)):
        del dic[i]["Probability"]
    return dic

##################################
######## MAIN
##################################
#Read json file
english = English()
english.readFile()
english.vocabulary = sortDictionaly(english.vocabulary)

#Study
english.vocabulary = quiz(english.vocabulary)

#Save to json file
english.vocabulary = deleteProbability(english.vocabulary)
english.saveFile()
