# -*- coding: utf-8 -*-
"""
Tue May  8 21:28:12 2018: Dhiraj
"""
#https://stats.stackexchange.com/questions/203740/logistic-regression-scikit-learn-vs-statsmodels
# module imports
from patsy import dmatrices
import pandas as pd
from sklearn.linear_model import LogisticRegression
import statsmodels.discrete.discrete_model as sm
import numpy as np

# read in the data & create matrices
df = pd.read_csv('https://stats.idre.ucla.edu/stat/data/binary.csv')
y, X = dmatrices('admit ~ gre + gpa + C(rank)', df, return_type = 'dataframe')
#y = ravel.column_or_1d(y, warn=True)
#y=y.reshape(-1,1)
y
X
# sklearn output
model = LogisticRegression(fit_intercept = True, C = 1e9)
mdl = model.fit(X, np.ravel(y))
model.coef_

# sm
logit = sm.Logit(y, X)
logit.fit().params
