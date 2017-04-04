
# coding: utf-8

# # Predicting Hypoglycemic Symptoms using Machine Learning

# <p>The goal of this project is to predict when a Type I diabetic may experience hypoglycemic problems by analysing 70 patients who recorded their eating, sleeping, and hypoglycemic problem behaviours over a period of time.</p>
# <p>Our dataset is pulled from [here](https://archive.ics.uci.edu/ml/datasets/Diabetes) which comes from the UCI Machine Learning Repository.</p>

# ### Library Imports

# In[2]:

import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt


# ### Data Imports

# In[3]:

DATA_FOLDER = './Diabetes-Data/'

get_ipython().magic('matplotlib inline')
fixed_df = pd.read_csv(DATA_FOLDER + 'data-01', sep='\t', names=['Date', 'Time', 'Number', 'Count'], header = None, parse_dates=[[0, 1]], index_col=0)
fixed_df[:8]


# In[ ]:



