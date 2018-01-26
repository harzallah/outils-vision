# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

m2 = np.loadtxt('/home/eniso/outils-vision/tutorial/data/data2.txt',delimiter=',')

idx1 = m2[:, 2] == 1
idx0 = m2[:, 2] == 0

classif = LogisticRegression()
X = m2[:,0:2]
y = m2[:,2]

classif.fit(X, y)
resp = classif.predict(X)


x1_min, x1_max = m2[:,0].min(), m2[:,0].max(),
x2_min, x2_max = m2[:,1].min(), m2[:,1].max(),
xx1, xx2 = np.meshgrid(np.linspace(x1_min, x1_max), np.linspace(x2_min, x2_max))


resp = classif.predict_proba(np.c_[xx1.ravel(), xx2.ravel()])
resp = resp[:,0].reshape(xx1.shape)


plt.scatter(m2[idx0,0], m2[idx0,1], c='r')
plt.scatter(m2[idx1,0], m2[idx1,1], c='b')
plt.contour(xx1, xx2, resp, [0.5], linewidths=1, colors='g'); 

plt.show()
