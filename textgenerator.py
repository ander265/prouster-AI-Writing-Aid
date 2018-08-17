import numpy as np
import pandas as pd
from keras.models import Sequential, Model, Input, load_model
from keras.layers import LSTM, TimeDistributed, Activation, Dense


class TextGenerator:

    def __init__(self, model_file, documents_file, key='docs'):
        self.documents = pd.read_hdf(documents_file, key)
        self.model = load_model(model_file)
        self.VOCAB_SIZE = len(list(set(self.documents)))
        self.chars = list(set(self.documents))
        self.ix_to_char = {ix: char for ix, char in enumerate(self.chars)}

    def generate_text(self, length=15):
        ix = [np.random.randint(self.VOCAB_SIZE)]
        y_char = [self.ix_to_char[ix[-1]]]
        X = np.zeros((1, length, self.VOCAB_SIZE))
        for i in range(length):
            X[0, i, :][ix[-1]] = 1
            # print(self.ix_to_char[ix[-1]], end="")
            ix = np.argmax(self.model.predict(X[:, :i+1, :])[0], 1)
            y_char.append(self.ix_to_char[ix[-1]])
        return ('. ').join(y_char)+'.'
