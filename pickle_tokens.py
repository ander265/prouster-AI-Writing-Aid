from keras.preprocessing.text import Tokenizer
from pickle import dump

def load_doc(filename):
    # open the file as read only
    file = open(filename, 'r')
    # read all text
    text = file.read()
    # close the file
    file.close()
    return text
 
# load
in_filename = 'sequences.txt'
def get_lines(in_filename):
    doc = load_doc(in_filename)
    lines = doc.split('\n')
    return lines
 
lines = get_lines(in_filename)
# integer encode sequences of words
tokenizer = Tokenizer()
tokenizer.fit_on_texts(lines)

dump(tokenizer, open('tokenizer.pkl', 'wb'))