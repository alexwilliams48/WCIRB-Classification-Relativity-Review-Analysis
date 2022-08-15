#!/usr/bin/env python
# coding: utf-8

# In[258]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel(r"C:\Users\alexw\OneDrive\Desktop\cr-state-2022_09_set-download_approved.xlsx", sheet_name = 1)
df.info()


# In[280]:


df.nlargest(10, 'Exposure - Year 1')


# In[264]:


df.corr()


# In[267]:


total_exposure = [df['Exposure - Year 1'].sum() + df['Exposure - Year 2'].sum() + 
df['Exposure - Year 3'].sum() + df['Exposure - Year 4'].sum() + df['Exposure - Year 5'].sum()]

print(total_exposure)


# In[281]:


def claims_yearone(x):
    for i in df['Class Code 1'].items():        
        if i[1] == x:
            sc1 = df.loc[i[0], 'Serious Number Claims - Year 1']
            nsc1 = df.loc[i[0], 'Non-Serious Number Claims - Year 1']
            claims_sum = sc1 + nsc1
            y = (sc1, nsc1) 
            mylabels1 = 'Serious Number Claims - Year 1',sc1  
            mylabels2 =  "Non-Serious Number Claims - Year 1", nsc1
            mylabels = mylabels1 , mylabels2
            plt.pie(y, labels = mylabels)
            title = x, "Year 1 Serious vs Non Serious Claims"
            plt.legend(title = title)
            plt.show()
            return
    print("Class Code", x, "was not found")

claims_yearone(8810)
claims_yearone(8742)
claims_yearone(8859)

