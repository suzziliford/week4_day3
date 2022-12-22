#Create a function that counts how many disctict words are in the string below, then outputs a dictionary with the words as the 
# key and the values as the amount of times that word appears in the string.

# create an algorithim that will count how many times each 
# word shows up and then displays a dictionary with those values (collections package has a feature does something similar)

a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'



def count_words(text):
    name_tally = {}
    for word in text.split(' '):
        name_tally[word] = text.count(word) 

    return name_tally
    # for word in text:
    #     if word == word:
            

    
print(count_words(a_text))


# If you think you need to loop with indices, first, ask yourself a question: do I even need some kind of counter as I'm looping? 
# If you don't need a counter, just use a for loop without any frills. But if you do need to count upward while looping, 
# you can use Python's built-in enumerate function to help you do that counting.
