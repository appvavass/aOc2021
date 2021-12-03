import pandas as pd
from pandas.core import series

def split_by_cha(string):
    return [c for c in string.rstrip("\n")]

def listToString(s): 
    str1 = ""   
    return (str1.join(s))

def oppositeMode(mode):
    if mode == '1': return '0'
    else: return '1'

def listToBinary(lst):
    lst.reverse()
    dec = 0
    i = 0
    for bit in lst:
        dec =  dec + bit*pow(2,i)
        i = i + 1
    return dec


fopen = open('input_day3.txt')

raw_data  = []
for lines in fopen:
    raw_data.append((split_by_cha(lines)))

df = pd.DataFrame(data=raw_data)
cols = []
for i in range(1,13):
    bit =  'bit' + str(i)
    cols.append(bit)
df.columns=cols

epsilon = []
gamma =  df.mode(axis=0).values.tolist()
gamma = gamma[0]
gamma = [int(i) for i in gamma]
for e in gamma:
    if e == 1: epsilon.append(0)
    else: epsilon.append(1)

gamma = listToBinary(gamma)
epsilon = listToBinary(epsilon)

print('part 1 answer is {}'.format(epsilon*gamma))

def filterframe(dataframe,gas,bitposition):
    column = 'bit'+str(bitposition)
    subset = dataframe[column]
        
    subset_mode = subset.mode().values
    subset_mode =  subset_mode[0]
    if gas =='oxygen':
        if subset.mode().shape[0] > 1:
            keep = '1'
        else: keep = subset_mode
    else:
        if subset.mode().shape[0] > 1:
            keep = '0'
        else:
            keep = oppositeMode(subset_mode) 
    
    new_df = dataframe[dataframe[column] == str(keep)]
    return new_df

df2 =  filterframe(df,'oxygen',1)
df1 = df


for i in range(1,13):
    df2 = filterframe(df1,'oxygen',i)
    if df2.shape[0] > 1:
        #print(df2.shape[0])
        df1 = df2
        #print('going to position', i+1)
        continue
    else:
        oxy_rate = df2.values.tolist()
        oxy_rate = oxy_rate[0]
        oxy_rate =  [int(e) for e in oxy_rate] 
        break

oxy_rate = listToBinary(oxy_rate)

df1 = df
for i in range(1,13):
    df2 = filterframe(df1,'co2',i)
    if df2.shape[0] > 1:
        df1 = df2
        continue
    else:
        co2_rate = df2.values.tolist()
        co2_rate = co2_rate[0]
        co2_rate =  [int(e) for e in co2_rate] 
        break

co2_rate = listToBinary(co2_rate)

print('part 2 answer is {}'.format(oxy_rate*co2_rate))