# working with curled source text # refs a file already in the same directory
import nltk                                 # there is a package called nltk. Load if for this file.

def open_file_and_get_text(filename):       # given a filename, openit
    with open(filename,'r') as our_file:
        text = our_file.read()
    return text              # takes the file, reads it. stores it as a string


#######

our_file = "eyre.txt"
text = open_file_and_get_text(our_file)



# take a long STRING and break it into words
words = nltk.word_tokenize(text)
print(words[0:30])


clean_words =[] #create an empty list called clean_words
for word in words:  # step through the list, do this
        clean_words.append(word.lower()) # append, one at a time, the new, lowercased word for each
print(clean_words[0:30])
