#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 11:23:20 2018

@author: hiteshady
"""

import pandas as pd
import numpy as np
import csv
train = pd.read_csv('E:\dataSets\events/household.csv', header = 0)
train.describe()
test1 = pd.read_csv('E:\dataSets\events/alert_type_1.csv', header = 0)
test2 = pd.read_csv('E:\dataSets\events/alert_type_2.csv', header = 0)
train.head()
train.isnull().sum()
test1.isnull().sum()
test2.isnull().sum()
test1['l'] = [x.split('_') for x in test1.id]
test1.head()
test2['l5'] = [x.split('_') for x in test2.id]
test2.head()
test1['hid'] = test1.l.apply(lambda x:x[0])
test1['hhid'] = test1.l.apply(lambda x:x[1])
test1['date'] = test1.l.apply(lambda x:x[2])
test1['hr'] = test1.l.apply(lambda x:x[3])
test2['hid5'] = test2.l5.apply(lambda x:x[0])
test2['hhid5'] = test2.l5.apply(lambda x:x[1])
test2['date5'] = test2.l5.apply(lambda x:x[2])
test2['hr5'] = test2.l5.apply(lambda x:x[3])
test1.head()
test2.head()
test1.isnull().sum()
test2.isnull().sum()
test1['date'] = pd.to_datetime(test1['date'])
test2['date5'] = pd.to_datetime(test2['date5'])
test1.isnull().sum()
test2.isnull().sum() #hites
test1['sec'] = (test1.date - pd.to_datetime("1/1/1970 00:00"))
test2['sec5'] = (test2.date5 - pd.to_datetime("1/1/1970 00:00"))
test1['sec1'] = test1.sec/np.timedelta64(1,'s')
test2['sec6'] = test2.sec5/np.timedelta64(1,'s')
test1['hr1'] = [int(x) for x in test1.hr]
test2['hr6'] = [int(x) for x in test2.hr5]
test1['sec2'] = test1.sec1 + test1.hr1*3600
test2['sec7'] = test2.sec6 + test2.hr6*3600
test1 = test1.drop(['id','l','date','hr','sec','sec1','hr1'],axis=1)
test2 = test2.drop(['id','l5','date5','hr5','sec5','sec6','hr6'],axis=1)
test1.isnull().sum()
test2.isnull().sum()
target = train.value
train = train.drop(['value'],axis=1)
tra = np.array(train,order='C',copy=False)
tar = np.array(target,order='C',copy=False)
tes = np.array(test1,order='C',copy=False)
tes1 = np.array(test2,order='C',copy=False)
from sklearn.ensemble import GradientBoostingRegressor
model = GradientBoostingRegressor(loss='lad',n_estimators=125,random_state=45,verbose=2,max_depth=8,subsample=0.8,learning_rate=0.3)
model = model.fit(tra,tar)
pred = model.predict(tes)
pred1 = model.predict(tes1)
pred[0:20]
pred1[0:20]
test1['value'] = pred
test2['value5'] = pred1
test2.head()
test3 = test1.groupby(['hid','hhid']).agg({'value':['mean','std']})
test3.head()
test3['s1'] = test3['value']['mean'] + test3['value']['std']
test3.head()
test4 = test3.to_dict()
test4
test4[('s1','')][('0','0')]
test1.head()
test1['alert'] = 0
test1.head()
for x in test1.hid.unique():
    for y in test1.hhid.unique():
        for i in list(test1.loc[(test1.hid==x) & (test1.hhid==y),'value'].index):
            if test1.loc[i,'value'] > test4[('s1','')][(x,y)]:
                test1.loc[i,'alert'] = 1
test1.head()
test1.loc[test1.alert==1,:].shape
test1.shape
sub1 = pd.read_csv('/Users/hiteshady/Documents/MUIT-PGD/Python/Python-Projects/sub1.csv', header = 0)
sub1.shape
sub1.head()
sub1['alert'] = test1.alert
sub1.head()
sub1.to_csv('F:/Sapient/alert_type_1.csv',index=False)
test3 = test2.groupby('hid5').agg({"value5":['mean','std']})
test3.head()
test3['s1'] = test3['value5']['mean'] + test3['value5']['std']
test3.head()
d1 = test3.to_dict()
d1
d1[('s1','')]['0']
test2['alert'] = 0
test2.head()
for x in test2.hid5.unique():
    for y in test2.hhid5.unique():
        for i in list(test2.loc[(test2.hid5==x) & (test2.hhid5==y),'value5'].index):
            if test2.loc[i,'value5'] > d1[('s1','')][x]:
                test2.loc[i,'alert'] = 1
test2.head()
test2.loc[test2.alert==1,:].shape