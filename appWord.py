from flask import Flask, render_template
from pickle import load
from keras.models import load_model
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
#print(tg)
app = Flask(__name__)

@app.route('/')
def index():
    text = tg.generate_seq()
    return render_template('website.html', neural_network_output=text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True, threaded=False)