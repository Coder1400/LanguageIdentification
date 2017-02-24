#Arken Ibrahim: amibrah2@illinois.edu

import re, sys
from collections import defaultdict
from math import log 



'''
Takes as input a list of strings (unigrams) and returns a dict of dicts
that contains the count for each occurrence of a bigram.

Accesses to keys that do not exist will return the default callable.
(i.e zero)

'''
def get_letter_bigrams(letters):
    counts = defaultdict(lambda: defaultdict(int))
    for (x, y) in zip( letters, letters[1:] ):
        counts[x][y]+=1
    return counts


'''

This is the main function responsible for calculating the probability for a
sentence. it takes the products of  P(Wn|Wn-1) = C(Wn-w, Wn) / C(Wn-1) for each
LETTER bigram in the string.

We apply LaPlace smoothing to this letter bigram model.

'''
def get_total_prob( input_str, counts):
    total_prob = 0;
    characters = list(input_str)
    for (k_1, k) in zip(characters, characters[1:]): # get letter bigrams from test data
        
        # here we calculate the bigram prob: P(Wn|Wn-1) = C(Wn-w, Wn) / C(Wn-1)
        # in other words we divide the occurences of the bigram by the occurences of the unigram Wn-1
        
        bigram_count = counts[k_1][k]
        unigram_count = sum(counts[k_1].values())
        
        # Add one smoothing is applied here -- LA PLACE :)
        prob = float(bigram_count + 1)/float(unigram_count + len(counts))
        total_prob += log(prob, 2) # compute probability in logspace
        
    return total_prob
        


if __name__ == '__main__':


    # Generate english language model
    lang_english_file = open("LangId.train.English")
    eng_tokens = list(lang_english_file.read().decode("utf-8"))
    eng_bigram_counts = get_letter_bigrams(eng_tokens)
    
    # Generate french language model
    lang_fr_file = open("LangId.train.French")
    fr_tokens = list(lang_fr_file.read().decode("utf-8"))
    fr_bigram_counts = get_letter_bigrams(fr_tokens)
    
    # Generate italian language model
    lang_ital_file = open("LangId.train.Italian")
    ital_tokens = list(lang_ital_file.read().decode("utf-8"))
    ital_bigram_counts = get_letter_bigrams(ital_tokens)
    
    
    
    # test data on each of the three models for each sentence and return highest prob.
    test_file = open("LangId.test")
    solution_file = open("letterLangId.out", 'w+') # output will be printed here
    
    line_number = 1
    for line in test_file.readlines():
        
        # test on english model
        eng_res = get_total_prob(line.decode("utf-8"), eng_bigram_counts)
        
        # test on english model
        fr_res = get_total_prob(line.decode("utf-8"), fr_bigram_counts)
        
        # test on english model
        ital_res = get_total_prob(line.decode("utf-8"), ital_bigram_counts)

        
        # print prediction
        prediction = max(eng_res, fr_res, ital_res)
        
        if prediction == eng_res: print >> solution_file, str(line_number) + " English"
        
        elif prediction == fr_res: print >> solution_file, str(line_number) + " French"
        
        else: print >> solution_file, str(line_number) + " Italian"
        
        line_number+=1


    # close handles
    
    lang_english_file.close()
    lang_fr_file.close()
    lang_ital_file.close()
    test_file.close()
    solution_file.close()





