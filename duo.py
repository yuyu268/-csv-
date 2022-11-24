import pandas as pd
import numpy as np
import itertools

url = 'https://raw.githubusercontent.com/yuyu268/-csv-/main/%E3%83%87%E3%83%A5%E3%82%AA%E9%AD%94%E6%B3%95.csv'

df_duo = pd.read_csv(url,index_col="番号")

print('所持しているSSRのカード番号（下記表参照）を入力してください（半角数字かつ空白で区切ってください）')
print('https://drive.google.com/file/d/1_aEasF394s2wMPYc5NT50QH7pWJKrJEN/view?usp=sharing')

b = list(map(int, input().split()))


#b = [32,48,50,45,29,19,38,33,46,13,35,7,34,2]　32 48 50 45 29 19 38 33 46 13 35 7 34 2

for i in range(2,6):
  b_pairs = (list(itertools.combinations(b,i)))

sco = list(range(len(b_pairs)))
nam = list(range(len(b_pairs)))

for i in range(0,len(b_pairs)):
  a = b_pairs[i]
  score = 0
  for k in range(0,5):
    y = df_duo["該当キャラ"].loc[a[k]]
    for j in range(0,5):
      z = df_duo["キャラ"].loc[a[j]]
      if (y == z):
        score = score+1
        break
    
  sco[i] = score
  nam[i] = a
  
a1 = np.array(nam)
b1 = np.array(sco)
sor = np.c_[a1,b1]
sor=sor.tolist()

print("")

for i1 in range(len(sor)):                                      
  for j1 in range(len(sor) - 1 - i1):
    if sor[j1][5] < sor[j1+1][5]:
      sor[j1], sor[j1+1] = sor[j1+1], sor[j1]

for i in range(0,5):
  print(i+1,"位")
  for j in range(0,5):
    print(df_duo["カード"].loc[sor[i][j]])
  print("　デュオ魔法:",sor[i][5],"回")
  print("")