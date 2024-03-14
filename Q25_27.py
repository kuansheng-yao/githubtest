#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 10:49:33 2023

@author: ju-tsetsai
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import plotly.io as io
io.renderers.default='browser'
import plotly.offline
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots

df = pd.read_csv(r'/Users/ju-tsetsai/Desktop/insurance.csv')

#練習25
#建立樞紐分析
df2 = pd.crosstab(df['Vehicle_Age'], df['Gender'])
df2.plot.bar(stacked=True)


# #練習26
# #建立百分比樞紐分析
# df2 = pd.crosstab(df['Vehicle_Age'], df['Gender'], normalize='index')
# df2.plot.bar(stacked=True)

# #練習27
# df1 = pd.crosstab(df['Vehicle_Age'], df['Gender'])
# df1.plot.barh(stacked=True)
# df2 = pd.crosstab(df['Vehicle_Age'], df['Gender'], normalize='index')
# df2.plot.barh(stacked=True)