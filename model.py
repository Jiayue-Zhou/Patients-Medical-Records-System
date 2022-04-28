# -*- coding: utf-8 -*-
"""BlockchainProject.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OlpfSxD34eNd3R-Ft9e9iV-9jnCF6Pmm
"""
import json
import time
import pandas as pd
import numpy as np
from hashlib import sha256

import imblearn

print(imblearn.__version__)
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import RandomOverSampler, SMOTE

num_features = [
    'hemoglobin',
    'platelets',
    'MPV',
    'RBC',
    'lymphocytes',
    'MCHC',
    'leukocytes',
    'basophils',
    'MCH',
    'eosinophils',
    'MCV',
    'monocytes',
    'RDW']
scaler = StandardScaler()


def algo(df, dp):
    df = pd.DataFrame(df)
    print(df.shape)
    #print(df)

    df[num_features] = scaler.fit_transform(df[num_features])

    #oversample = RandomOverSampler(sampling_strategy=1)

    smt = SMOTE(sampling_strategy=0.5,k_neighbors = 5,random_state = 1206)

    y = df['covid19_Res']
    X = df.drop(['covid19_Res'], axis=1)
    X.head()

    #X_over, y_over = oversample.fit_resample(X, y)


    # X_train, X_test, y_train, y_test = train_test_split(X_over, y_over, test_size=0.20, random_state=1206,
    #                                                     stratify=y_over)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=1206,
                                                        stratify=y)

    X_over,y_over=smt.fit_resample(X_train,y_train)

    hyperPara = {'C': [10], 'gamma': [0.1], 'kernel': ['rbf'], 'shrinking': [True]}
    #svm1 = SVC(C=10, gamma=0.1, kernel='rbf')

    svm1=SVC(C=10,gamma = 0.1,kernel='rbf',class_weight = {1:10})

    svm1.fit(X_train, y_train)
    #print(X_test)
    y_pred = svm1.predict(X_test)
    print(f'size: {len(y_pred)}')
    print(y_pred)
    y_pred = svm1.predict(dp)
    print(y_pred[0])
    print(f'You are {dp}')
    if (y_pred[0] == 0):
        y_pred = "Negative"
    elif (y_pred[0] == 1):
        y_pred = "Positive"
    print(f'The AI predict you are {y_pred}!')
    from sklearn.metrics import classification_report

    y_pred_2 = svm1.predict(X_test)
    print(f'Result is {classification_report(y_test, y_pred_2)}')


#
# """#Just use this to find hyperparameters DNU!!!!!!!"""
#
# param_gridSVM = {'C': [0.1, 1, 10, 100, 1000],
#                  'shrinking': [True, False],
#                  'gamma': ['scale', 'auto', 1, 0.1, 0.01, 0.001, 0.0001],
#                  'kernel': ['linear', 'poly', 'rbf', 'sigmoid']}
# gridSVM = GridSearchCV(cv=5, estimator=SVC(class_weight='balanced', random_state=101), param_grid=param_gridSVM,
#                        refit=True, verbose=1, scoring='balanced_accuracy', n_jobs=3)
# gridSVM.fit(X_train, y_train)
#
# # print(gridSVM.best_params_)
# if __name__ == '__main__':
#     df = pd.read_csv('C:/Users/zjy/Desktop/Final_dataset_covid19.csv')
#     print(df)
#     #algo(df)
