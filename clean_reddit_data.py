import pandas as pd 


def clean_reddit_data(directory):
    data = pd.read_table(directory, header=None)
    data['prefix'] = data[0].apply(lambda x: str(x).split(']')[0][1:])
    data['prompt'] = data[0].apply(lambda x: str(x).split(']')[-1])
    return data.drop(columns=0, inplace=True)
