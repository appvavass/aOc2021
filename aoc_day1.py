import pandas as pd

inputfile = 'input_day1_pt1.txt'

df = pd.read_csv(inputfile, header=None)
df.columns = ['depth']

def answer_1(datafr,startpoint):
    godown = 0
    for i in range(startpoint,(datafr.shape[0]-1)):
        grad = int(datafr.iloc[i+1]-datafr.iloc[i])
        if grad > 0:
            godown = godown + 1
        else: continue

    return godown

sliding_window = 3
df2 = df.rolling(sliding_window).sum()

print(answer_1(df,0))
print(answer_1(df2,2))

