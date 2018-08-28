import os
import requests

def get_pickle():
    if not os.path.isfile('tokenizer.pkl'):
        response = requests.get('https://s3-us-west-2.amazonaws.com/jared.b.anderson/https://s3-us-west-2.amazonaws.com/jared.b.anderson/tokenizer.pkl')
        with open('tokenizer.pkl','wb') as f:
            f.write(response.content)