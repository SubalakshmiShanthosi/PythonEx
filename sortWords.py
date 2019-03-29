#To sort the given sentence's words in ascending order

inputString=input("Enter the input String : ")
print("Sorting the input string words in ascending order :")
wordList=list(inputString.split(" "))
wordList.sort()
print(wordList)
