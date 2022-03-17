"""plot for linear regression"""

# TODO move to a separate file
# import libraries

import sklearn
import sys

import matplotlib.pyplot as plt # graph
import numpy as np # number handling
import pandas as pd # structured data handling
import sklearn.linear_model
import os

# enable this when running locally
from utils import save_fig

from matplotlib.pyplot import figure

#figure(figsize=(4.5, 3.5), dpi=80)
plt.figure(figsize=(5,4))
# linear regression sample data set and plot

# First plot
training_data = {
    'x':[1,2,4],
    'y':[1,3,3]}

plt.axis([0, 5, 0, 4])
plt.plot(training_data['x'], training_data['y'],'bo')
plt.xlabel("x")
plt.ylabel("y")
plt.text(2, 1.5, "x: {}".format(training_data['x']), fontsize=14, color="b")
plt.text(2, 1.0, "y: {}".format(training_data['y']), fontsize=14, color="b")
plt.text(2, 0.5, "When x = 3, what will be y?", fontsize=14, color="r")
plt.grid()

save_fig("linear_regression_example_1")
X = X=np.linspace(0, 5, 50)
plt.plot(X, 0.7*X+1, "g")
x_new = 3
plt.plot(x_new, 0.7*x_new+1, "ro")
save_fig("linear_regression_example_2")

# Clear Figure
plt.clf()
plt.axis([0, 5, 0, 4])
plt.plot(training_data['x'], training_data['y'],'bo')
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.plot(X, 0.7*X+1, "g")
plt.plot(X, 0.3*X+2, "r")
# plt.plot(X, 0.3*X+2, "g")
plt.text(2, 1.5, "f(x) = 0.7x + 1", fontsize=14, color="g")
plt.text(2, 1.0, "f(x) = 0.3X + 2", fontsize=14, color="r")
plt.text(2, 0.5, r"Find $w_1$, $w_2$ in $f(x) = w_1X + w_2$", fontsize=14, color="b")
save_fig("linear_regression_example_3")
# plt.show()


# Clear Figure
plt.clf()
plt.axis([0, 5, 0, 4])
plt.plot(training_data['x'], training_data['y'],'bo')
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
w = [0.7, 1]
plt.plot(X, w[0]*X+w[1], "g")

for i in range(len(training_data)+1):
    plt.plot([training_data['x'][i], training_data['x'][i]],
             [training_data['y'][i], w[0]*training_data['x'][i]+w[1]], 'r-')

plt.text(1.1, 1.5, "residual", fontsize=14, color="r")
save_fig("linear_regression_example_4")


# plot for non linear dataset
plt.clf()

x = np.arange(0,5,0.2)
x_data = x
x.shape
noise = np.random.normal(loc=0.0, scale=0.4, size=x.shape[0])


y = -.25*(x-2.5)*(x-2.5) + 3
y+= noise

training_data = {
    'x':x, 
    'y':y}

plt.clf()
plt.axis([0, 5, 0, 4])
plt.plot(training_data['x'], training_data['y'] ,'bo')
plt.xlabel("x")
plt.ylabel("y")
plt.grid()

save_fig("linear_regression_example_5")

