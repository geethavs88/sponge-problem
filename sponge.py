def sponge_case(sentence):
    # Write your solution here!
    words = sentence.split()
    new_sentence = []
    for word in words:
        new_word = spong_case_word(word)
        new_sentence.append(new_word)
    return " ".join(new_sentence)

def spong_case_word(word):
    new_word = word[0].lower()
    for i in range(1, len(word)):
        if i%2 == 0:
            new_word += word[i].lower()
        else:
            new_word += word[i].upper() 
    print(new_word)       
    return new_word           

    

    
#initialize a variable called newword with lowercase of first letter
# convert the first letter to lowercase and store it to newword
#Iterate  through each letter of the word
# if index is odd change it to uppoer case
# if index is even change it to lower case.


#if there are more than one word in the sentence
# split the sentence using .split() and store the words to alist
# loop through each word of the list 
# call sponge case function for each word
# Store the value to a new sentence






# Test cases
assert sponge_case("spongebob") == "sPoNgEbOb"
assert sponge_case("Who are YOU calling A Pinhead") == "wHo aRe yOu cAlLiNg a pInHeAd"
assert sponge_case("WHAT is UP my dude") == "wHaT iS uP mY dUdE"
assert sponge_case("E") == "e"
assert sponge_case("e") == "e"

print("All tests passed!")
print("Discuss time and space complexity if there's time remaining")