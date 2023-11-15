# Luke Scott
# COSC 311
# Project 1
# Dr. Wang

import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from matplotlib import pyplot as plt
import pandas as pd
from warnings import simplefilter
import seaborn as sns; sns.set()

simplefilter(action='ignore', category=FutureWarning)

wifi = pd.read_fwf('wifi_localization.txt', header=None,
                   names=['s1', 's2', 's3', 's4', 's5', 's6', 's7', 'room'])

room_one = wifi[wifi['room'] == 1]
room_two = wifi[wifi['room'] == 2]
room_three = wifi[wifi['room'] == 3]
room_four = wifi[wifi['room'] == 4]

'''
plt.scatter(x = room_one['s1'], y = room_one['s2'], color = 'y')
plt.scatter(x = room_two['s1'], y = room_two['s2'], color = 'g')
plt.scatter(x = room_three['s1'], y = room_three['s2'], color = 'b')
plt.scatter(x = room_four['s1'], y = room_four['s2'], color = 'r')

plt.legend(['room 1', 'room 2', 'room 3', 'room 4'])
plt.title('Signal Strength to IP 1 and 2')
'''
knn = KNeighborsClassifier(n_neighbors = 4)

X = wifi[['s1', 's2', 's3', 's4', 's5', 's6', 's7']].values

Y = wifi['room'].values

Y[Y == 1] = 1
Y[Y == 2] = 2
Y[Y == 3] = 3
Y[Y == 4] = 4

knn.fit(X, Y)
dt = DecisionTreeClassifier(criterion='entropy')
dt.fit(X, Y)

# Task 1

print('Sample data for testing : [-50, -60, -70, -80, -70, -60, -50]')

knn_num_wrong = np.sum(np.not_equal(knn.predict(X), Y))
print('KNN prediction of sample data:\n',knn.predict([[-50, -60, -70, -80, -70, -60, -50]]))
print('KNN prediction of X:\n',knn.predict(X))
print(f'The KNN model got {knn_num_wrong} wrong')
print('The KNN model scored',knn.score(X, Y))


knn_cm = confusion_matrix(Y, knn.predict(X))
print('Confusion matrix and classification report for knn model:\n',knn_cm)
print(classification_report(Y, knn.predict(X)))

dt_num_wrong = np.sum(np.not_equal(dt.predict(X), Y))
print('DT prediction of sample data:\n',dt.predict([[-50, -60, -70, -80, -70, -60, -50]]))
print('DT prediction of X:\n',dt.predict(X))
print(f'The DT model got {dt_num_wrong} wrong')
print('The DT model scored',dt.score(X, Y))

dt_cm = confusion_matrix(Y, dt.predict(X))
print('Confusion matrix and classification report for dt model:\n',dt_cm)
print(classification_report(Y, dt.predict(X)))

# Task 2

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=.3, random_state=0)

split_knn = KNeighborsClassifier(n_neighbors = 4)
split_knn.fit(X_train, Y_train)
knn_y_pred = split_knn.predict(X_test)

knn_split_num_wrong = np.sum(np.not_equal(split_knn.predict(X), Y))
print("KNN Split prediction of sample data:\n",split_knn.predict([[-50, -60, -70, -80, -70, -60, -50]]))
print("KNN Split prediction of X:\n",split_knn.predict(X))
print(f'The KNN model got {knn_split_num_wrong} wrong')
print('The KNN model scored',split_knn.score(X_test, Y_test))

knn_split_cm = confusion_matrix(Y, split_knn.predict(X))
print('Confusion matrix and classification report for split knn model:\n',knn_split_cm)
print(classification_report(Y, split_knn.predict(X)))

clf = DecisionTreeClassifier(max_depth = 4, random_state = 0, criterion = 'entropy')
clf.fit(X_train, Y_train)
clf_y_pred = clf.predict(X_test)

clf_num_wrong = np.sum(np.not_equal(clf.predict(X), Y))
print('DT Split prediction of sample data:\n',clf.predict([[-50, -60, -70, -80, -70, -60, -50]]))
print('DT Split prediction of X:\n',clf.predict(X))
print(f'The DT model (after split) got {clf_num_wrong} wrong')
print('The DT model (after split) scored',clf.score(X_test, Y_test))

dt_split_cm = confusion_matrix(Y, clf.predict(X))
print('Confusion matrix and classification report for dt split model:\n',dt_split_cm)
print(classification_report(Y, clf.predict(X)))

mat = confusion_matrix(split_knn.predict(X), Y)
sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False,
            xticklabels=range(1, 5),
            yticklabels=range(1, 5))
plt.xlabel('true label')
plt.ylabel('predicted label')
plt.show()

mat2 = confusion_matrix(clf.predict(X), Y)
sns.heatmap(mat2.T, square=True, annot=True, fmt='d', cbar=False,
            xticklabels=range(1, 5),
            yticklabels=range(1, 5))
plt.xlabel('true label')
plt.ylabel('predicted label')
plt.show()

clf_best = DecisionTreeClassifier(max_depth = 5, random_state = 0, criterion = 'gini', min_samples_leaf = 5, min_samples_split = 5)
clf_best.fit(X_train, Y_train)
print(clf_best.score(X_test, Y_test))
print(classification_report(Y, clf_best.predict(X)))
bestmat = confusion_matrix(clf_best.predict(X), Y)
sns.heatmap(bestmat.T, square=True, annot=True, fmt='d', cbar=False,
            xticklabels=range(1, 5),
            yticklabels=range(1, 5))
plt.xlabel('true label')
plt.ylabel('predicted label')
plt.show()

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=.1, random_state=0)

clf10 = DecisionTreeClassifier(max_depth = 4, random_state = 0, criterion = 'entropy')
clf10.fit(X_train, Y_train)
clf10_y_pred = clf10.predict(X_test)
clf10_score = clf10.score(X_test, Y_test)
print(classification_report(Y, clf10.predict(X)))

mat3 = confusion_matrix(clf10.predict(X), Y)
sns.heatmap(mat3.T, square=True, annot=True, fmt='d', cbar=False,
            xticklabels=range(1, 5),
            yticklabels=range(1, 5))
plt.xlabel('true label')
plt.ylabel('predicted label')
plt.show()

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=.2, random_state=0)

clf20 = DecisionTreeClassifier(max_depth = 4, random_state = 0, criterion = 'entropy')
clf20.fit(X_train, Y_train)
clf20_y_pred = clf20.predict(X_test)
clf20_score = clf20.score(X_test, Y_test)
print(classification_report(Y, clf20.predict(X)))

mat4 = confusion_matrix(clf20.predict(X), Y)
sns.heatmap(mat4.T, square=True, annot=True, fmt='d', cbar=False,
            xticklabels=range(1, 5),
            yticklabels=range(1, 5))
plt.xlabel('true label')
plt.ylabel('predicted label')
plt.show()

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=.3, random_state=0)

clf30 = DecisionTreeClassifier(max_depth = 4, random_state = 0, criterion = 'entropy')
clf30.fit(X_train, Y_train)
clf30_y_pred = clf30.predict(X_test)
clf30_score = clf30.score(X_test, Y_test)
print(classification_report(Y, clf30.predict(X)))

mat5 = confusion_matrix(clf30.predict(X), Y)
sns.heatmap(mat5.T, square=True, annot=True, fmt='d', cbar=False,
            xticklabels=range(1, 5),
            yticklabels=range(1, 5))
plt.xlabel('true label')
plt.ylabel('predicted label')
plt.show()

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=.4, random_state=0)

clf40 = DecisionTreeClassifier(max_depth = 4, random_state = 0, criterion = 'entropy')
clf40.fit(X_train, Y_train)
clf40_y_pred = clf40.predict(X_test)
clf40_score = clf40.score(X_test, Y_test)
print(classification_report(Y, clf40.predict(X)))

mat6 = confusion_matrix(clf40.predict(X), Y)
sns.heatmap(mat6.T, square=True, annot=True, fmt='d', cbar=False,
            xticklabels=range(1, 5),
            yticklabels=range(1, 5))
plt.xlabel('true label')
plt.ylabel('predicted label')
plt.show()

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=.5, random_state=0)

clf50 = DecisionTreeClassifier(max_depth = 4, random_state = 0, criterion = 'entropy')
clf50.fit(X_train, Y_train)
clf50_y_pred = clf50.predict(X_test)
clf50_score = clf50.score(X_test, Y_test)
print(classification_report(Y, clf50.predict(X)))

mat7 = confusion_matrix(clf50.predict(X), Y)
sns.heatmap(mat7.T, square=True, annot=True, fmt='d', cbar=False,
            xticklabels=range(1, 5),
            yticklabels=range(1, 5))
plt.xlabel('true label')
plt.ylabel('predicted label')
plt.show()

scores = [clf10_score, clf20_score, clf30_score, clf40_score, clf50_score]
print(scores)
plt.bar(['10%', '20%', '30%', '40', '50'], scores, edgecolor = 'black', color = 'lightblue')
plt.ylim([0.9, 1])
plt.show()