#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 13:50:50 2023

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
import squarify

df = pd.read_csv(r'/Users/ju-tsetsai/Desktop/insurance.csv')

#練習28
df_sum = df.groupby("Vehicle_Age", as_index=False).sum()
plt.pie(df_sum["Annual_Premium"], labels=df_sum["Vehicle_Age"],
        autopct="%1.1f%%")
plt.show()

# #練習29
# df_sum = df.groupby("Vehicle_Age", as_index=False).sum()
# fig = go.Figure(data=[go.Pie(labels=df_sum["Vehicle_Age"],
#                              values=df_sum["Annual_Premium"])]) 
# fig.show()


# #練習30
# # Pie圖表部分 
# df_sum = df.groupby("Vehicle_Age", as_index=False).sum()
# fig = go.Figure(data=[go.Pie(labels=df_sum["Vehicle_Age"],
#                              values=df_sum["Annual_Premium"],
#                              hole=0.5)]) 
                              
# # 圖表標題與甜甜圈部分的文字 
# fig.update_layout(title_text="Total Annual Premium Contribution by Vehicle Age",
#                   annotations=[{
#                                 "text": "Contribution Percentage",
#                                 "x": 0.5,
#                                 "y": 0.5,
#                                 "font_size": 20,
#                                 "showarrow": False}]) 
# # 顯示圖表 
# fig.show()