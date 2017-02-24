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
def get_word_bigrams(words_list):
    counts = defaultdict(lambda: defaultdict(int))
    for (x, y) in zip( words_list, words_list[1:] ):
        counts[x][y]+=1
    return counts





'''
Get the frequency of frequencies of a given bigram dictionary. Used for GOOD-TURING smoothing 
'''
def get_bigram_freq_of_freq(counts, freq):
    return sum( 1 for c in counts.values() for x in c.values() if x == freq )





'''
This is the main function responsible for calculating the probability for a
sentence. it takes the products of  P(Wn|Wn-1) = C(Wn-w, Wn) / C(Wn-1) for each
bigram in the string.

GOOD-TURING SMOOTHING:
In this example we will apply the Good-Turing smoothing technique, using
an upper threshold of 20. Check page 103 of the textbook for an explanation of the formula used. 

'''
THRESHOLD = 20

def get_total_prob( input_str, counts, total_bigram_count, freq_of_freq):
    total_prob = 0;
    words = input_str.split()
    
    for (k_1, k) in zip(words, words[1:]): # get letter bigrams from test data
        
        # here we calculate the bigram prob: P(Wn|Wn-1) = C(Wn-w, Wn) / C(Wn-1)
        # in other words we divide the occurences of the bigram by the occurences of the unigram Wn-1
        
        bigram_count = counts[k_1][k]
        unigram_count = sum(counts[k_1].values())
        
        
        # calculcate c* for all bigrams that have count less than the upper threshold
        if (bigram_count <= THRESHOLD):
            
            # 0 occurrence bigrams should take the probability of one occurrence bigrams
            if bigram_count == 0:
                bigram_n_plus_1_count  = freq_of_freq[0]
                prob = float(bigram_n_plus_1_count)/float(total_bigram_count)

            # apply discounted count for bigram counts 0 < c <= 5 -> check textbook for equation
            else:
                
                freq_n_plus_1 =  freq_of_freq[bigram_count] # Nc+1
                freq_n = freq_of_freq[bigram_count - 1]     # Nc
                
                freq_k_plus_one = freq_of_freq[THRESHOLD]   # Nk+1
                freq_1 = freq_of_freq[1 - 1]                # N1
                
                
                # plug into threshold/GT formula
                c_discount = float(bigram_count + 1) * (float(freq_n_plus_1) / float(freq_n))
                threshold_normalization =  ((THRESHOLD + 1) * float(freq_k_plus_one)) / float(freq_1) 
                denominator = float(1) - threshold_normalization
                
                # new disocunted bigram count: c*
                bigram_discount = (c_discount - (bigram_count * threshold_normalization)) / (denominator)
                prob = float(bigram_discount)/float(unigram_count)
        else:
            prob = float(bigram_count)/float(unigram_count)
            
            
        total_prob += log(prob, 2) # compute probability in logspace
        
    return total_prob
        


if __name__ == '__main__':


     # Generate english language model
    lang_english_file = open("LangId.train.English") 
    eng_tokens = lang_english_file.read().decode("utf-8").split() # split file into string tokens
    eng_bigram_counts = get_word_bigrams(eng_tokens)              # Generate dictionary of all bigrams
    total_eng_bigram_count = (len(eng_tokens)-1)**2               # number of all bigrams in corpus
    eng_freq_of_freq = [ get_bigram_freq_of_freq(eng_bigram_counts, x) for x in range(1, 22) ]   # list of freq of freq to be used by Good turing smoothing

  
    
    # Generate french language model
    lang_fr_file = open("LangId.train.French")
    fr_tokens = lang_fr_file.read().decode("utf-8").split()
    fr_bigram_counts = get_word_bigrams(fr_tokens)
    total_fr_bigram_count = (len(fr_tokens)-1)**2
    fr_freq_of_freq = [ get_bigram_freq_of_freq(fr_bigram_counts, x) for x in range(1, 22) ]

    
    
    # Generate italian language model
    lang_ital_file = open("LangId.train.Italian")
    ital_tokens = lang_ital_file.read().decode("utf-8").split()
    ital_bigram_counts = get_word_bigrams(ital_tokens)
    total_ital_bigram_count = (len(ital_tokens)-1)**2
    ital_freq_of_freq = [ get_bigram_freq_of_freq(ital_bigram_counts, x) for x in range(1, 22) ]

    
    
    # test data on each of the three models for each sentence and return highest probability
    test_file = open("LangId.test")
    solution_file = open("wordLangId2.out", 'w+') # output will be printed here
    
    line_number = 1
    for line in test_file.readlines():
        
        # --- Each model simulation gets passed in the precalculated frequency of frequencies for that specific model -----
        
        # get prob. from english model
        eng_res = get_total_prob(line.decode("utf-8"), eng_bigram_counts, total_eng_bigram_count, eng_freq_of_freq)
        
        # get prob. from french model
        fr_res = get_total_prob(line.decode("utf-8"), fr_bigram_counts, total_fr_bigram_count, fr_freq_of_freq)
        
        # get prob. from italian model
        ital_res = get_total_prob(line.decode("utf-8"), ital_bigram_counts, total_ital_bigram_count, ital_freq_of_freq)
    
        
        # show prediction
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
    solution_file.close