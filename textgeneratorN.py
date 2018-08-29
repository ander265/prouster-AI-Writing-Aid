from random import randint
from pickle import load
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
import keras.backend

def load_doc(filename):
    # open the file as read only
    file = open(filename, 'r')
    # read all text
    text = file.read()
    # close the file
    file.close()
    return text

class WordGenerator:

    def __init__(self, model_file, documents_file, token_file, key='docs'):
        self.model = load_model(model_file)
        self.documents = load_doc(documents_file)
        self.tokenizer = load(open(token_file, 'rb'))
        self.lines = self.documents.split('\n')
        self.seq_length = len(self.lines[0].split()) - 1

    def generate_seq(self, n_words=50, in_text=None):
        result = list()
        if in_text is None:
            in_text = self.lines[randint(0,len(self.lines))]
        # generate a fixed number of words
        for _ in range(n_words):
            # encode the text as integer
            encoded = self.tokenizer.texts_to_sequences([in_text])[0]
            # truncate sequences to a fixed length
            encoded = pad_sequences([encoded], maxlen=self.seq_length,
                                    truncating='pre')
            # predict probabilities for each word
            yhat = self.model.predict_classes(encoded, verbose=0)
            # map predicted word index to word
            out_word = ''
            for word, index in self.tokenizer.word_index.items():
                if index == yhat:
                    out_word = word
                    break
            # append to input
            in_text += ' ' + out_word
            result.append(out_word)
        #keras.backend.clear_session()
        return ' '.join(result)

tg = WordGenerator(
    model_file='results/model.h5', 
    documents_file='results/sequences.txt',
    token_file='results/tokenizer.pkl',
    key='docs')

print(tg.generate_seq(n_words=20))
print(tg.generate_seq(n_words=20))