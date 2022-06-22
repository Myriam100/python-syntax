# this should print "HELLO", "HEY", "YO", and "YES"
"""this is my docstring



"""

def print_upper_words(words):
    for word in words:
        print(word.upper())
        

def must_start_with(words, letters):
    for word in words:
        for letter in letters:
            if word.startswith(letter):
                print(word.upper())
                


print(print_upper_words(["hello", "hey", "goodbye", "yo", "yes"]))
print(must_start_with(["hello", "hey", "goodbye", "yo", "yes","apple","cat"],{"y", "a"}))