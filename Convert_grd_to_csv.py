
import numpy as np
import pandas as pd
import os

os.chdir('D:\\MY-DOC\\Documents\\Work\\EPIC\\Thesis-2')
source = 'Rainfall_Data_Source'
dest = 'Dest_Daily'

#Converting binary data into numbers (line 14)
#Then reshaping it according to shape on IMD Pune site
#Finally storing in a dataframe and saving it
os.chdir(source)
c=0
for file in os.listdir():
    f = open(file, "r")
    a = np.fromfile(f, dtype=np.float32)
    #Reading as numbers
    b = a.reshape(241,281)
    df = pd.DataFrame(b)
    
    df.to_csv(dest+"\\"+file+".csv",index = False)
    
    c+=1
    if c%10 == 0:
        print(c)
    
    
