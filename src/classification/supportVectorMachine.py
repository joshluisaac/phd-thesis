import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# To split the dataset into train and test datasets
from sklearn.model_selection import train_test_split
# To model the Gaussian Navie Bayes classifier
from sklearn.naive_bayes import GaussianNB
# To calculate the accuracy score of the model
from sklearn.metrics import accuracy_score


from sklearn import svm

url = "/home/joshua/Desktop/datascience/data_analysis_2/data_set.csv"

# Assign colum names to the dataset
names = ['CustomerId_PKEY','CustomerName_OPT','InvoiceDate_NN','InvoiceStatus_OPT','label']

# Read dataset to pandas dataframe
dataset = pd.read_csv(url, sep='|', names=names)

#gnb = GaussianNB()

gnb = svm.SVC()

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values

features_train, features_test, target_train, target_test = train_test_split(X, y, test_size = 0.33, random_state = 10)

#gnbClf.fit(X,y)
#pred = gnbClf.predict([[1,1,1,1]])

model = gnb.fit(features_train,target_train)
target_pred = gnb.predict(features_test)

print("New data point",gnb.predict([[1,0,0,0]]))

accuracy = accuracy_score(target_test, target_pred, normalize = True)

#print features_test
#print target_pred
#print dataset.describe()
print accuracy