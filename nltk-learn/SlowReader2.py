import nltk, re, pprint #  unclear if needed
# READ FILE

def open_file_and_get_text(filename):
    with open(filename,'r') as our_file:
        text = our_file.read()
    return text  # takes the file, reads it. stores it as a string

our_file = "walden.txt"
text = open_file_and_get_text(our_file)
w_words = nltk.word_tokenize(text)
w_sents = nltk.sent_tokenize(text)



ctr = 0
while ctr < 5:
    s_max_len = 100  # max of sentences ot permit
    t_len = (len(w_sents[ctr]))

    if ((t_len <s_max_len)):
        print(f"Sentence number {ctr} ")
        print(len(w_sents[ctr]))
        print(w_sents[ctr])
    ctr = ctr + 1



# w_words is now a list
#print("These are words")
#print(w_words[0:30]) # prints first 29 items in List

# nltk_walden_text = nltk.Text(w_words)

######### CONCORDANCE EXAMPLE ########
#print(nltk_walden_text.concordance("bottom"))
# adding variable to test it

#bottom_concord = (nltk_walden_text.concordance("bottom"))
#print(bottom_concord)


## TESTING DISPERSION PLOT
## NOTE THAT you need an NLTK object rather than a simple list to run nltk proesss on it.
# COMMENT THIS NEXT LINE IF DESIRED

#nltk_walden_text.dispersion_plot(['bottom','pond'])





# TOKENIZE file

# FORM SENTENCES - group tokens into list of sentence strings

# SUB SELECT - form a list of sentences incl. "word-x"

# DISPLAYER - increment through the subselect, on sentence at a Time
