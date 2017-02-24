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

1.) My word bigram language model implementation, with LaPlace smoothing,  was able to correctly predict the test data at a rate of <strong> 99.00% </strong>! There were only three instance where my program incorrectly predicted an input sentence. 

3.) It seems as though the letter bigram model produced SLIGHTLY better results than the word bigram model (only .66%)! However I do not think that that means that the letter bigram model is better overall. 



