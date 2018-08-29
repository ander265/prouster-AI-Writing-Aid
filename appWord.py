from flask import Flask, render_template, request
from pickle import load
from keras.models import load_model
import keras.backend
import tensorflow as tf
from download_model import download_model
from get_pickle import get_pickle
import textgeneratorN

download_model()
get_pickle()

tg = textgeneratorN.WordGenerator(
    model_file='results/model.h5', 
    documents_file='results/sequences.txt',
    token_file='results/tokenizer.pkl',
    key='docs')

#text = tg.generate_seq()
#print(tg)
app = Flask(__name__)
def init():
    global model,graph
    # load the pre-trained Keras model
    model = load_model('results/model.h5')
    graph = tf.get_default_graph()

@app.route('/')
def index():
    text = str.capitalize(tg.generate_seq(n_words = 20)+'...')
    return render_template('website.html', 
                neural_network_output=text)

# @app.route('/submit')
# def submit():
#     request._get_current_object

if __name__ == '__main__':
    print(("* Loading Keras model and Flask starting server...",
    "please wait until server has fully started"))
#    init()
    app.run(host='0.0.0.0', port=8080, debug=False, threaded=False)