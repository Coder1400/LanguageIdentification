Language Modeling: letter & word bi-grams for language identification.

Assignment 2: Ling 406

Arken Ibrahim
netid: amibrah2

========================== SETUP INSTRUCTIONS ===============================

1.) clone this repository https://github.com/Arken94/LanguageIdentification.git from github (I have added you as a collaborator).

2.) Within the newly cloned repository on your local machine, there should be 3 python files: “letterLangId.py”, “wordLangId.py”, and “wordLandId2.py”

3.) letterLangId.py is the letter bigram implementation. wordLangId.py is the word bigram implementation. wordLangId2.py is the word bigram implementation with an advanced smoothing technique (extra credit). 

4.) To run any of these python files simply run the file using the python command, for example: 

	“python wordLangId.py“

the code will open the proper training and test data files (hardcoded, no arguments to the program are needed) and implement the language model for that specific implementation. 

5.) NOTE: when you run any of the python files MAKE SURE that each of the training files and the test files exist in the same directory that you are running the python file from. I have included them in the github repository, so they should already be there. 

6.) the output of each program is printed to an output file with the same name as the python file, except with a “.out” extension. For example, wordLangId.py will print its output to wordLangId.out. These files should already contain the output of each program. 

7.) Please let me know if you have any questions or concerns about how to run the code. Enjoy :)



========================== ANALYSIS & ANSWERS ===============================

1.) My letter bigram language model implementation was able to correctly predict the test data at a rate of <strong> 99.66% </strong>! There was only one instance where my program incorrectly predicted an input sentence. 

I do believe that the letter bigram model CAN be implemented without any kind of smoothing, however I do not believe that adding a smoothing technique betters the results. I decided to use smoothing in my letter bigram model because I was afraid that there may have been some strange sequence of letters that wasn’t in the training data but that might have been in the test data. Since the number of letters, including punctuation and whitespace characters, was less than 100, I am sure that if no smoothing was applied, that the results would not be significantly worse. It is also important to note that many of the bigrams may have not needed to be smoothed because that specific sequence of letters is not allowed in language. For instance, “qt” is a sequence of letters that practically never appear in the english language. Therefore there is no need to smooth it. However I found that smoothing in general generated better results in this case!

2.) My word bigram language model implementation, with LaPlace smoothing,  was able to correctly predict the test data at a rate of <strong> 99.00% </strong>! There were only three instance where my program incorrectly predicted an input sentence. 

ANALYSIS: It seems as though the letter bigram model produced SLIGHTLY better results than the word bigram model (only .66%)! However I do not think that that means that the letter bigram model is better overall. The training data for the letter bigram was a good size (it contained many of the possible sequences of letters that the language could possibly contain), however I do not believe that the training data was sufficiently large for the word bigram models. There exists may more possibilities of word bigrams that could have been tested that were not present in the training data. Furthermore, I checked how many times the letter bigram model had to rely on smoothing for non existent bigrams vs the times that the word bigram model relied on smoothing for non existent bigrams. I found that the word bigram model had many more cases in which it relied on the smoothing technique to produce a probability for non existent bigrams - this of course is less reliable than actual data from the training set, and therefore I believe that this may have also hurt the performance of the word bigram model as well. 


3.) EXTRA CREDIT: My word bigram language model implementation, with Good Turing smoothing,  was able to correctly predict the test data at a rate of <strong> 99.66% </strong>! There was only one instance where my program incorrectly predicted an input sentence. 

I was very surprised to see that the Good-turing smoothing technique actually improved the performance of the word bigram model! It only incorrectly predicted one sentence, while the La Place version predicted three sentences incorrectly. I implemented the good turing smoothing technique using an upper threshold (20). For any bigram with a count less than 20, I would recalculate its count (discounted count) using the Good-Turing formula. And for every bigram that had a count greater than the threshold, I simply kept its count the same and did nothing special. Please check on page. 103 of the textbook for the exact equation that I used! 

I think that this smoothing technique provided better results because it did not shift the probability mass of all the bigrams but rather it only redistributed the probability mass of bigrams with count <= 20 in order to account for bigrams that have never been seen! 


I truly loved doing this MP, and am looking forward to many more like it. Thanks!




