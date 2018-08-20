import pandas as pd 


def clean_source_data(directory):
    data = pd.read_table(directory, header=None)
    data['prefix'] = data[0].apply(lambda x: str(x).split(']')[0][1:].strip())
    data['prompt'] = data[0].apply(lambda x: str(x).split(']')[-1].strip())
    data.drop(columns=0, inplace=True)
    data = data[-data['prefix'].isin(['IP','OT','PM','MP','PI','CC'])]
    data.reset_index(inplace=True, drop=True)
    return data