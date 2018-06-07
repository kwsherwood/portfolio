import nltk, re, pprint     #  unclear if needed
from time import sleep      # python module to use sleep, delay

dur = 0.5         # set sleep variable for use in delay. see sleep() below
s_max_len = 100 # setting global variable for max lenght of sentence
s_max_num = 20  #    counter for how many sentences will be displayed

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
        if ((t_len <s_max_len)):
            print(sh_sents[ctr])
        ctr = ctr + 1
        sleep(dur) # Time in seconds.
# ----------------------------------------
our_file = "walden.txt"
text = open_file_and_get_text(our_file)         # w_words = nltk.word_tokenize(text) # nltk list for working words
w_sents = nltk.sent_tokenize(text)              # nltk list of all sentences
# nb w_sents is a List, w_words is also a list NOT a string. sentence_printer(w_sents) # calls sentence printer function

u_word = input("Choose one word to slow read from Walden: ")

print("You typed", len(nltk.word_tokenize(u_word)), "words: ",u_word) # var u_word is now available for driving the program

sentence_user_choice(w_sents,u_word) # passes user input word to function that calculates if it is in the sentence.
