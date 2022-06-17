# Link: https://www.hackerrank.com/challenges/predicting-office-space-price/problem
# GitHub: https://github.com/vlwdan
# Developer: Daniel Lopes
# Score: 10.0

# Importing libraries
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Reading and splitting the data into training and testing data
F, N = map(int, input().split())
train = np.array([input().split() for i in range(N)], float)
T = int(input())
test = np.array([input().split() for i in range(T)], float)

# Setting Polynomial Features
XtoP = PolynomialFeatures(degree=3)

# Setting the model LinearRegression
model = LinearRegression()

# Creating model
model.fit(XtoP.fit_transform(train[:, :-1]), train[:, -1])

# Getting the result and showing it on the screen
ans = model.predict(XtoP.fit_transform(test))
print(*ans, sep='\n')
