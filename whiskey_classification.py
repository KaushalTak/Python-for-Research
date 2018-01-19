# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 17:07:28 2018

@author: Kaushal
"""

import numpy as np

import pandas as pd

whisky = pd.read_csv("whiskies.txt")

whisky["Region"] = pd.read_csv("regions.txt")

whisky.head()

whisky.iloc[0:10]

whisky.iloc[5:10, 0:5]

whisky.columns

flavors = whisky.iloc[:, 2:14]

#Correlation

corr_flavors = pd.DataFrame.corr(flavors)

import matplotlib.pyplot as plt
plt.figure(figsize = (10, 10))
plt.pcolor(corr_flavors)
plt.colorbar()
plt.savefig("corr_flavors.pdf")





corr_whiskey = pd.DataFrame.corr(flavors.transpose())
plt.figure(figsize = (10, 10))
plt.pcolor(corr_whiskey)
plt.axis("tight")
plt.colorbar()
plt.savefig("corr_whiskey.pdf")

#Clustering whiskies
#Spetral co-clustering

from sklearn.cluster.bicluster import SpectralCoclustering

model = SpectralCoclustering(n_clusters = 6, random_state = 0)

model.fit(corr_whiskey)

model.row_labels_
model.rows_

np.sum(model.rows_, axis=1)

np.sum(model.rows_, axis=0)


