# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 23:42:32 2018

@author: Ranjan
"""
import pandas as pd
import numpy as np
import math

df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm',
'Budapest_PaRis', 'Brussels_londOn'],
'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
'12. Air France', '"Swiss Air"']})

print("\n")
print("Before Processing . . . ")
print("\n")
print(df)
# point # 1 where it is required to replace NaNs by previous number adding 10
ctr=0
for t in df.iloc[:,1]:
    if math.isnan(t):
        df.iloc[ctr,1]=df.iloc[ctr-1,1]+10
    ctr+=1

# point # 1 continued to convert the col into integer from Float
df["FlightNumber"]=df["FlightNumber"].astype(int)

# point # 2 to split the col "From_to"
df_tmp = pd.DataFrame(index=range(0,len(df)))

df_tmp["From"]=df["From_To"].str.split('_').str.get(0)
df_tmp["To"]=df["From_To"].str.split('_').str.get(1)

# point # 3 to standardize the words in both separated cols
df_tmp["From"]=df_tmp["From"].str.lower()
df_tmp["From"]=df_tmp["From"].str.capitalize()

df_tmp["To"]=df_tmp["To"].str.lower()
df_tmp["To"]=df_tmp["To"].str.capitalize()

# point # 4 to delete the "From_To" col and attach the temporary DataFrame
df=pd.concat([df,df_tmp],axis=1)
df=df.drop("From_To",1)

print("\n")
print("After Processing . . . ")
print("\n")
print(df)

# point # 5 has not been done

