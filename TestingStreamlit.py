# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 10:34:25 2023

@author: Filmon Teweldemedhin Gebremichael
"""

import streamlit as st
import numpy as np
import pandas as pd
import glob
import warnings
import imp

warnings.filterwarnings('ignore')

files = glob.glob('*.txt')

li = []

for f in files:
    temp_df = pd.read_csv(f, delimiter= "\t", skiprows= 1)
    li.append(temp_df)
    print(f'Successfully created dataframe for {f} with shape {temp_df.shape}')

df = pd.concat(li, axis=0, ignore_index=True)
print(df.shape)
df
st.altair_chart(df)


