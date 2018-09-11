from flask import Flask, render_template, request
import string
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

bad_words = ['adolf','hitler', 'neonazi', 
            'donald','trump',
            'satan', 'depression',
            'suicide', 'rape']
conjunctions = ['m','t','s', 'd', 
            're','nt','ve','ll']

app = Flask(__name__)
def init():
    global model,graph
    # load the pre-trained Keras model
    model = load_model('results/model.h5')
    graph = tf.get_default_graph()

@app.route('/')
def index():
    text = str.title(tg.generate_seq(n_words = 10)+'...')
    for profanity in [word.title() for word in bad_words]:
        text = text.replace(profanity, 'Galvanize')
    for letter in [c.title() for c in conjunctions]:
        cutoff = ' '+letter+' '
        end = ' ' + letter + '.'
        if (cutoff) in text:
            text = text.replace(cutoff,"'"+letter.lower()+" ")
        elif end in text:
            text = text.replace(end, "'"+letter.lower()+".")
    return render_template('index.html', 
                feedback = request.args.get('response'),
                neural_network_output=text)

# @app.route('/text/', methods=['GET', 'POST'])
# def submit():
#     feedback = None
#     if request.method == 'GET':
#        if request.form['response']:
#             feedback = request.form['response']
#             #requests.args.GET 
#     return render_template('index.html', 
#                 feedback = feedback)

if __name__ == '__main__':
    print(("* Loading Keras model and Flask starting server...",
    "please wait until server has fully started"))
    app.run(host='0.0.0.0', port=8080, debug=False, threaded=False)