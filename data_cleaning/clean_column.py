#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def clean_column(file_name, column_names_lst):
    df = pd.read_csv(file_name)
    for column in column_names_lst:
        lst = df[column].to_list()
        w=[]
        for l in lst:
            a = re.sub(r'[^[\w\s]', '', l)
            w.append(a)
        df[column]=w
    
    return df

