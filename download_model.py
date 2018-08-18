import os
import requests

def download_model():
    if not os.path.isfile('tg.h5'):
        response = requests.get('https://s3-us-west-2.amazonaws.com/jared.b.anderson/tg.h5')
        with open('tg.h5','wb') as f:
            f.write(response.content)