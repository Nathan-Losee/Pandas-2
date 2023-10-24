import pandas as pd
import numpy as np
#1
def euc_dist(a, b):
    # Ensure both points have the same dimension
    if len(a) != len(b):
        raise ValueError("Need to be the same length")
    squared_dif = (a - b) ** 2
    distance = (squared_dif.sum()) ** 0.5
    return distance
p = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
q = pd.Series([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
q_1 = euc_dist(p,q)
print('q_1: ', q_1)

#2
df = pd.DataFrame(np.arange(20).reshape(-1, 5), columns=list('abcde'))
q_2 = df[['c', 'b', 'a', 'd', 'e']]
print('q_2: ', q_2)

#3
df = pd.DataFrame(np.arange(20).reshape(-1, 5), columns=list('abcde'))
def column_switcharoo(df, col1, col2):
    new_col1 = df.columns.get_loc(col1)
    new_cos2 = df.columns.get_loc(col2)
    columns = list(df.columns)
    columns[new_col1], columns[new_cos2] = columns[new_cos2], columns[new_col1]
    new_df = df[columns]
    return new_df
q_3 = column_switcharoo(df, 'a', 'c')
print('q_3:', q_3)

#4
df = pd.DataFrame(np.random.random(4)**10, columns=['random'])
print(df.head())
def supression(x):
    return x.apply(lambda y: '{:.4f}'.format(y))
df['random'] = supression(df['random'])
q_4 = df
print('q_4:', q_4)

#5
def euc_dista(row1, row2):
    return np.linalg.norm(row1 - row2)
df = pd.DataFrame(np.random.randint(1,100, 40).reshape(10, -1), columns=list('pqrs'), index=list('abcdefghij'))
nearest = df.apply(lambda row: df.drop(index=row.name).apply(lambda x: (x.name, euc_dista(row, x)), axis=1).min(), axis=1)
df['nearest_row'] = [info[0] for info in nearest]
df['distance'] = [info[1] for info in nearest]
print('q_5:',df)

#6
data = {'A': [45, 37, 0, 42, 50],
        'B': [38, 31, 1, 26, 90],
        'C': [10, 15, -10, 17, 100],
        'D': [60, 99, 15, 23, 56],
        'E': [76, 98, -0.03, 78, 90]
        }
df = pd.DataFrame(data)

q_6 = df.corr()
print('q_6:', q_6)