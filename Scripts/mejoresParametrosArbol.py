# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from numpy import genfromtxt
from sklearn.tree import DecisionTreeClassifier



X_train= genfromtxt("../Datos/DAtos_train/movil/X_train_movil_aplaudir.csv", delimiter=',')
y_train= genfromtxt("../Datos/DAtos_train/movil/y_train_movil_aplaudir.csv", delimiter='')
X_train[np.isnan(X_train)] = np.median(X_train[~np.isnan(X_train)])
X_val= genfromtxt("../Datos/DAtos_val/X_val_movil_aplaudir.csv", delimiter=',')
y_val= genfromtxt("../Datos/DAtos_val/y_val_movil_aplaudir.csv", delimiter='')
X_val[np.isnan(X_val)] = np.median(X_val[~np.isnan(X_val)])


x = min_samples_split = [0.001, 0.01, 0.025, 0.1, 0.2, 0.5, 50, 25, 10, 2]
split_len = len(min_samples_split)
y = min_samples_leaf = [0.001, 0.01, 0.025, 0.1, 0.2, 0.5, 50, 25, 10, 2, 1]
leaf_len = len(min_samples_leaf)

precision = 0
split = 0
leaf = 0
max_por = 0

for i in range(split_len):
    for j in range(leaf_len):
        clf = DecisionTreeClassifier(criterion='entropy',random_state=0, min_samples_split = min_samples_split[i], min_samples_leaf = min_samples_leaf[j])
        clf = clf.fit(X_train, y_train)
        precision = clf.score(X_val ,y_val)*100
        if precision > max_por:
            max_por = precision
            split = min_samples_split[i]
            leaf = min_samples_leaf[j]

print("\n\nMáxima precisión(Accuracy): {},\nmin_samples_split: {}, min_samples_leaf: {}".format(max_por, split, leaf))