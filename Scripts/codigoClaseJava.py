#! /usr/bin/python

import numpy as np
import pandas as pd
from numpy import genfromtxt
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import _tree


X = genfromtxt("./X_train_movil.csv", delimiter=',')
y = genfromtxt("./y_train_movil.csv", delimiter='')

clf = DecisionTreeClassifier(criterion='entropy', max_depth=6, random_state=0, min_samples_split=2, min_samples_leaf=2)
clf = clf.fit(X, y)

def maximovalor(arr):
    maximo = 0
    for i in range(len(arr)):
        if(arr[i] > arr[maximo]):
            maximo = i
    return maximo

def tree_to_code(tree, feature_names, codigo):
    tree_ = tree.tree_
    feature_name = [
        feature_names[i] if i != _tree.TREE_UNDEFINED else "undefined!"
        for i in tree_.feature
    ]
    #print "def tree({}):".format(", ".join(feature_names))

    def recurse(node, depth, codigo):
        indent = "  " * depth
        if tree_.feature[node] != _tree.TREE_UNDEFINED:
            name = feature_name[node]
            threshold = tree_.threshold[node]
            codigo = codigo + "if((double)df.get(i, \"{}\") <= {})\n".format(name, threshold)
            codigo = recurse(tree_.children_left[node], depth + 1, codigo)
            codigo = codigo + "else //if({} > {})\n".format(name, threshold)
            codigo = recurse(tree_.children_right[node], depth + 1, codigo)
        else:
            a = maximovalor(tree_.value[node][0])
            codigo = codigo + "return {};\n".format(int(a + 1))
        return codigo
        
    codigo = recurse(0, 1, codigo)
    return codigo

feature_names=[ 'gyro_alpha_avg','gyro_beta_avg','gyro_gamma_avg','accel_x_avg','accel_y_avg','accel_z_avg','gyro_alpha_min','gyro_beta_min','gyro_gamma_min','accel_x_min','accel_y_min','accel_z_min','gyro_alpha_max','gyro_beta_max','gyro_gamma_max','accel_x_max','accel_y_max','accel_z_max','gyro_alpha_std','gyro_beta_std','gyro_gamma_std','accel_x_std','accel_y_std','accel_z_std','xy_cor','xz_cor','yz_cor','x_fft','y_fft','z_fft','gyro_alpha_med','gyro_beta_med','gyro_gamma_med','accel_x_med','accel_y_med','accel_z_med']
codigo = "public void miMetodo(){\n"

codigo = tree_to_code(clf,feature_names, codigo)

codigo = codigo + "\n}"

print(codigo)
