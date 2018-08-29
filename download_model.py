import os
import requests

def download_model():
    if not os.path.isfile('model.h5'):
        response = requests.get('https://s3-us-west-2.amazonaws.com/jared.b.anderson/model.h5')
        with open('model.h5','wb') as f:
            f.write(response.content)
