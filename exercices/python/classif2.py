# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

data = loadmat('MNIST_sample.mat')

y = data['y']
X = np.c_[data['X']]

sample = np.random.choice(X.shape[0], 10)
plt.imshow(X[sample,:].reshape(-1,20).T)
plt.axis('off');
plt.figure()
sample = np.random.choice(X.shape[0], 10)
plt.imshow(X[sample,:].reshape(-1,20).T)
plt.axis('off');
plt.figure()
sample = np.random.choice(X.shape[0], 10)
plt.imshow(X[sample,:].reshape(-1,20).T)
plt.axis('off');
plt.show()

# Split : 80% train, 20% test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

print 'Number of training example : ', X_train.shape[0]
print 'Number of testing example : ', X_test.shape[0]

# lancer l'apprentissage sur 

