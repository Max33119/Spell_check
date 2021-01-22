# Spell Check Starter

import re



def main():
    # Load data files into lists
    dictionary = loadWordsFromFile("data-files/dictionary.txt")
    aliceWordsFull = loadWordsFromFile("data-files/AliceInWonderLand.txt")

    #print(dictionary[0:50])
    #print(aliceWordsFull[0:50])

    loop = True
    while loop:
        selection = getMenuSelection()

        #single word search
        if selection == "1":
            word = input("Please enter a word: ")
            search_type = input("Select a search algorithm (linear/binary): ")

            # find what algorithim is used
            if search_type.lower() == "linear":
                #linear search function
                index = single_linear(dictionary, word)
                if index != -1:
                    print(word + " is in the dictionary at position " + str(index))
                else:
                    print(word + " is not in the dictionary")

            elif search_type.lower() == "binary":
                #binary search function
                binary_index = single_binary(dictionary, word)
                if binary_index != -1:
                    print(word + " is in the dictionary at position " + str(binary_index))
                else:
                    print(word + " is not in the dictionary")

            else:
                print("returning to main menu")

        elif selection == "2":
            search_type = input("Select a search algorithm (linear/binary): ")

            #find type of search
            if search_type.lower() == "linear":
                alice_linear(aliceWordsFull, dictionary)
            elif search_type.lower() == "binary":
                alice_binary(aliceWordsFull, dictionary)
            else:
                print("returning to main menu")
        elif selection == "3":
            loop = False

    print("Goodbye")

# end main()


def getMenuSelection():
    print("\nMAIN MENU")
    print("1: Single word spell check")
    print("2: Alice in wonderland spell check")
    print("3: Exit")
    return input("Enter menu selection: ")




def loadWordsFromFile(fileName):
    # Read file into an array of words
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()

    return re.findall(r"[\w]+", textData)



#linear word checking------------------------------------------------------------------------

def single_linear(aList, selected_word):
    for i in range(len(aList)):
        if aList[i] == selected_word:
            return i
    
    return -1

#binary word checking-----------------------------------------------------------------------------------------------------

def single_binary(aList, selected_word):
    lowerIndex = 0
    upperIndex = len(aList) - 1


    while lowerIndex <= upperIndex:
        middleIndex = (lowerIndex + upperIndex) // 2
        if selected_word == aList[middleIndex]: 
            return middleIndex
        elif selected_word < aList[middleIndex]:
            upperIndex = middleIndex - 1
        else:
            lowerIndex = middleIndex + 1

    return -1

#option2 linear alice in wonderland checking--------------------------------------------------------------------------------------------------

def alice_linear(aList, dictionary):
    count = 0
    for word in aList:
        found = single_linear(dictionary, word.lower())
        if found != -1:
            pass
        else:
            count += 1
            print(word + " is an unknown word")
    
    print("total words unknown are: " + str(count))

#option2 binary alice in wonderland checking----------------------------------------------------------------------------------------------------

def alice_binary(aList, dictionary):
    count = 0
    for word in aList:
        found = single_binary(dictionary, word.lower())
        if found != -1:
            pass
        else:
            count += 1
            print(word + " is an unkown word")

    print("total words unkown are: " + str(count))

# Call main() to begin program
main()
