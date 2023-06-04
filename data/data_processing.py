dataFolder='../data/'

import pandas as pd
#import numpy as np
raw = pd.read_csv(dataFolder+"raw data/XBB.csv", names=["raw"])

#a=r_alpha.loc[r_alpha["alpha raw"]==">hCoV-19/Japan/PG-253383/2021|EPI_ISL_14108484|2021-05-12"]

def convert_tuple(o_tuple):  
  str=''  
  for k in o_tuple:  
    str=str+k
  return str  

index=[[]]*141


i=-1
j=-1
for row in raw.itertuples(index=False, name=None):
    i+=1
    n_row = convert_tuple(row)
    if ">" in n_row:
        j+=1
        index[j] = i


#print(index[0])
#print(index[2])


#for m in index:
   # print(m)

final_list = [[]]*140


for m in range(0,140): 
    new = []
    final = []
    for k in range(index[m]+1, index[m+1]):
        n_row = convert_tuple(raw.iloc[k])
        new += n_row
    
    final = "".join(new)
    final_list[m] = final


    
#for m in range(0, 100):
    #for k in range(index[m]+1, index[m+1]):
    #print(row) #each row is a tuple
        #n_row = convert_tuple(raw.iloc[k])
        #new[m].append(n_row)


df = pd.DataFrame(final_list)


df.to_csv("sequences.csv", mode="a", index=False, header=False)

#df.to_csv("alpha_new.csv", mode="a", index=False, header=False)


data = pd.read_csv(dataFolder+"sequences.csv", names=["sequences"])

