import pandas as pd

df = pd.read_csv('input_day2.txt',names=['instruction','distance'],sep=' ')
directions = df.groupby('instruction').sum()
hor = directions.loc['forward']
vert = directions.loc['down']-directions.loc['up']
ans1 = hor*vert

def lookup(i,aim, depth, hor):
    if df.at[i,'instruction'] == 'forward':
        hor = hor + df.at[i,'distance']
        depth =  depth + aim* df.at[i,'distance']
    elif df.at[i,'instruction'] == 'up':
        aim = aim - df.at[i,'distance']
    else: aim = aim + df.at[i,'distance']

    return aim, depth, hor

aim = 0
depth = 0
hor = 0

for i in range(0,df.shape[0]):
    aim, depth,hor = lookup(i,aim,depth,hor)

print('answer',depth*hor)