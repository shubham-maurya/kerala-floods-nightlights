
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd
import os
import re
#Need to aggregate daily data into monthly

os.chdir('D:\\MY-DOC\\Documents\\Work\\EPIC\\Thesis-2\\Rainfall_Data_Source')


# In[52]:


#Have 6 unique months - 082017, 092017, 102017, 082018, 092018, 102018
mmyyyy_combos = ['082017.grd.csv','092017.grd.csv','102017.grd.csv','082018.grd.csv','092018.grd.csv','102018.grd.csv']
for mmyyyy in mmyyyy_combos:
    selected_files = list(filter(lambda x: x.endswith(mmyyyy), os.listdir('Dest_Daily')))
    df = pd.read_csv('Dest_Daily\\'+selected_files[0])
    for i,file in enumerate(selected_files):
        
        if i == 0:
            continue
            
        df2 = pd.read_csv('Dest_Daily\\'+file)
        #Adding daily rainfall
        df=df.add(df2,fill_value=0)

    df.to_csv('Dest_Monthly\\'+mmyyyy+'.csv',index=False)

