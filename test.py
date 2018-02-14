import pandas as pd
allData = pd.read_csv('consumerPrices.csv')

data1 = allData[['都道府県','食料','水道光熱費']]
#print(data1.head())

import matplotlib.pyplot as plt
#matplotlib inline
plt.scatter(data1['食料'],data1['水道光熱費'])
plt.xlabel('Food')
plt.ylabel('Fuel,Light,Water charges')
plt.show()

from sklearn.cluster import KMeans
model1 = KMeans(n_clusters=4, random_state=0)
data1_X = data1[['食料','水道光熱費']]
model1.fit(data1_X)
y1 = model1.labels_
print(y1)

