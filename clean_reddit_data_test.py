import pandas as pd 

PREFIXES = ['WP','EU','CW','TT','RF']
def clean_source_data(path_to_file):
    data = pd.read_table(path_to_file, header=None)
    data['prefix'] = data[0].apply(lambda x: str(x).split(']')[0][1:].strip()).str.upper()
    data['prompt'] = data[0].apply(lambda x: str(x).split(']')[-1].strip())
    data['prompt'] = data['prompt'].apply(lambda x: str(x).strip('"').replace('``','"').replace("''",'"'))
    data.drop(columns=0, inplace=True)
    #undesired tags: (['IP','OT','PM','MP','PI','CC'])]
    data = data[data['prefix'].isin(PREFIXES)]
    data.reset_index(inplace=True, drop=True)
    data.dropna(inplace=True)
    return data

data = clean_source_data('data/writingPrompts/test.wp_source')

prompts_as_str = []
prompts_as_txt = []
prompts_as_csv = []

for prefix in PREFIXES:
    prompts_as_str.append(data['prompt'][data['prefix']==prefix].str.cat(sep = '  '))
    prompts_as_txt.append(data['prompt'][data['prefix']==prefix])
    prompts_as_csv.append(data['prompt'][data['prefix']==prefix])

for prefix, prompts in zip(PREFIXES,prompts_as_str):
    with open('data/strings/'+prefix+'sT.txt', "w") as text_file:
        text_file.write(prompts)

for prefix, prompts in zip(PREFIXES,prompts_as_txt):
    prompts.to_csv('data/writingPrompts/'+prefix+'T.txt',index=False)

for prefix, prompts in zip(PREFIXES,prompts_as_csv):
    prompts.to_csv('data/writingPrompts/'+prefix+'T.csv',index=False)
