# -*- coding: utf-8 -*-
"""
Tue May  8 17:19:23 2018: Dhiraj
"""
# dataset import
from sklearn import datasets
#scikit-learn has few small std dataset that do not require to download any file from some external site

# Load the diabetes dataset
diabetes = datasets.load_diabetes()
diabetes

boston = datasets.load_boston()
boston

iris = datasets.load_iris()
iris

digits = datasets.load_digits()
digits

linnerud = datasets.load_linnerud()
linnerud

wine = datasets.load_wine()
wine

breast_cancer = datasets.load_breast_cancer()
breast_cancer


#%%
#Sample Images

image1 = datasets.load_sample_images()
image1


#load_sample_image(image_name)
