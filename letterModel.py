import re, sys

if len(sys.argv) < 2:
    print "Plese pass in the name of a file!"
    sys.exit()
test_filename = sys.argv[1] # this is the name of the <strong> test </strong> filename.

# we first need to create three language models, one for each set of training data.












f = open(filename) # open the file using python's standard file library
text = f.read() # extract the file's contents to a string, in order to match the regex against it!
