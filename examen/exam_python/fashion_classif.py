# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.read_csv('fashion-mnist_test.csv')

y = data['label'].values
X = data.drop(['label'], axis = 1).values


# Split : 80% train, 20% test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

print 'Number of training example : ', X_train.shape[0]
print 'Number of testing example : ', X_test.shape[0]


