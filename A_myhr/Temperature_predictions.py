import numpy as np
import pandas as pd

n = int(input())
colnames = list(input().strip().split())

l1 = []
l2 = []
for i in range(0, n):
    x = list(input().strip().split())
    l1.append(x[2])
    l2.append(x[3])

ll1 = [np.nan if 'Missing' in i else float(i) for i in l1]

int1 = pd.Series(ll1).interpolate(method='cubic', order=2)

ll2 = [np.nan if 'Missing' in i else float(i) for i in l2]

int2 = pd.Series(ll2).interpolate(method='cubic', order=2)
   
res = pd.DataFrame({'item':np.array(l1)[np.array(['Missing' in i for i in l1])], 'value':list(int1[['Missing' in i for i in l1]])})
res = res.append(pd.DataFrame({'item':np.array(l2)[np.array(['Missing' in i for i in l2])], 'value':list(int2[['Missing' in i for i in l2]])}))
res1 = pd.DataFrame({'index':list(res.item.apply(lambda x: int(x.split('_')[1]))), 'value':res.value})
res1 = res1.sort_values(by=['index'])
x = res1.value.tolist()

for i in range(0, len(x)):
    print("%.2f" % x[i])