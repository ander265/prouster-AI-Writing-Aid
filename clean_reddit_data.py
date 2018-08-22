import pandas as pd 

PREFIXES = ['WP','EU','CW','TT','RF']
def clean_source_data(directory):
    data = pd.read_table(directory, header=None)
    data['prefix'] = data[0].apply(lambda x: str(x).split(']')[0][1:].strip()).str.upper()
    data['prompt'] = data[0].apply(lambda x: str(x).split(']')[-1].strip())
    data.drop(columns=0, inplace=True)
    #undesired tags: (['IP','OT','PM','MP','PI','CC'])]
    data = data[data['prefix'].isin(PREFIXES)]
    data.reset_index(inplace=True, drop=True)
    data.dropna(inplace=True)
    #data['chars'] = data['prompt'].apply(lambda x: sorted(''.join(set((str(x))))))
    return data

data = clean_source_data('writingPrompts/train.wp_source')

prompts_as_txt = []
for prefix in PREFIXES:
    prompts_as_txt.append(data['prompt'][data['prefix']==prefix].str.cat(sep = '  '))

for prefix, prompts in zip(PREFIXES,prompts_as_txt):
    with open('writingPrompts/'+prefix+'.txt', "w") as text_file:
        text_file.write(prompts)

