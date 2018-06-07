import nltk, re, pprint     #  unclear if needed
from time import sleep      # python module to use sleep, delay

dur = .1         # set sleep variable for use in delay. see sleep() below
s_max_len = 50 # setting global variable for max lenght of sentence
s_max_num = 100  #    counter for how many sentences will be displayed

def open_file_and_get_text(filename):
    with open(filename,'r') as our_file:
        text = our_file.read()
    return text  # takes the file, reads it. stores it as a string

def sentence_printer(sh_sents):
    ctr = 0
    while ctr < s_max_num:
        t_len = (len(sh_sents[ctr]))
        if ((t_len <s_max_len)):
            print(sh_sents[ctr])
        ctr = ctr + 1
        sleep(dur) # Time in seconds.

def sentence_user_choice(sh_sents,key_word):
    # key_word sthis variable is now available for use
    ctr = 0
    while ctr < s_max_num:
        t_len = (len(sh_sents[ctr]))
        k_value = sh_sents[ctr].find(key_word)
        if (k_value > -1):
            if ((t_len <s_max_len)):
                # sh_sents is a list, as I step through it, I need to
                # check if it contains the passed variable *key_word*
                print(sh_sents[ctr])
                print("\n")
                print("\n")
        ctr = ctr + 1
        sleep(dur) # Time in seconds.

# ----------------------------------------
our_file = "walden.txt"
text = open_file_and_get_text(our_file)         # w_words = nltk.word_tokenize(text) # nltk list for working words
w_sents = nltk.sent_tokenize(text)              # nltk list of all sentences # nb w_sents is a List, w_words is also a list NOT a string. sentence_printer(w_sents) # calls sentence printer function
u_word = input("Choose one word to slow read from Walden: ")
print("You typed the ", len(nltk.word_tokenize(u_word)), "word: ",u_word, "\n Slow Reader will now find sentences.") # var u_word is now available for driving the program

sentence_user_choice(w_sents,u_word) # passes user input word to function that calculates if it is in the sentence.
