# Link: https://www.hackerrank.com/challenges/battery/problem
# GitHub: https://github.com/vlwdan
# Developer: Daniel Lopes
# Score: 10.0

# Importing libraries
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
#import matplotlib.pyplot as plt

# Importing dataset
df = pd.read_csv('trainingdata.txt', names=['charged', 'lasted'])

# Converting each column into float
df['charged'] = df['charged'].astype(float)
df['lasted'] = df['lasted'].astype(float)

# Ploting the graph with data
#x_plot = df['charged']
#y_plot = df['lasted']
#plt.scatter(x_plot,y_plot)
#plt.show()

# Removing constant part
df = df[df['charged'] <= 4.0]

# Ploting the graph with the new data
#x_plot = df['charged']
#y_plot = df['lasted']
#plt.scatter(x_plot,y_plot)
#plt.show()

# Separating the data into independent and dependent variables
# Converting each column into a numpy array
x = np.array(df['charged']).reshape(-1, 1)
y = np.array(df['lasted']).reshape(-1, 1)

# Splitting the data into training and testing data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25)

model = LinearRegression()
 
model.fit(x_train, y_train)
#print(model.score(x_test, y_test))

# Using model 
timeCharged = float(input())
ans = model.predict([[timeCharged]])
if timeCharged >= 4:
    ans = 8.0
else:
    ans = round(ans[0][0],2)
print(ans)
