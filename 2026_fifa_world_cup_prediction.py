# -*- coding: utf-8 -*-
"""2026_FIFA_World_Cup_Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12Z7lpcYNYIXWBBhKT_DJcpMHpEpQPkKk
"""

import pandas as pd
teams = pd.read_csv('teams.csv')

teams

# delete extra column
teams = teams[["Team", "Year", "Athletes", "Age", "Win", "Prev_win"]]

teams

# checar si se pueden hacer predicciones
teams.corr()['Win']

import seaborn as sns
sns.lmplot(x = "Year", y ="Win", data = teams, fit_reg = True, ci = None)

# we compare both graphs
import seaborn as sns
sns.lmplot(x = "Athletes", y ="Win", data = teams, fit_reg = True, ci = None)

teams.plot.hist(y='Win')

teams[teams.isnull().any(axis=1)]

teams = teams.dropna()
teams

# split data
train = teams[teams['Year'] < 2018].copy()
test = teams[teams['Year'] >= 2018].copy()

train.shape

test.shape

# Training the model

from sklearn.linear_model import LinearRegression
reg = LinearRegression()

predictors = ['Athletes', 'Prev_win']
target = 'Win'

# fitting the regresssion model
reg.fit(train[predictors], train['Win'])
LinearRegression()

predictions = reg.predict(test[predictors])
predictions

test['predictions'] = predictions
test

test.loc[test['predictions'] < 0, 'predictions'] = 0
test['predictions'] = test['predictions'].round()

test

from sklearn.metrics import mean_absolute_error
error = mean_absolute_error(test['Win'], test['predictions'])
error

teams.describe()['Win']

test[test['Team'] == 'Mexico']

test[test['Team'] == 'Argentina']

errors = (test['Win'] - test['predictions']).abs()
errors

error_by_team = errors.groupby(test['Team']).mean()
error_by_team

wins_by_team = test['Win'].groupby(test['Team']).mean()

error_ratio = error_by_team / wins_by_team
error_ratio

error_ratio[~pd.isnull(error_ratio)]

import numpy as np
error_ratio = error_ratio[np.isfinite(error_ratio)]
error_ratio

error_ratio.plot.hist()

error_ratio.sort_values()