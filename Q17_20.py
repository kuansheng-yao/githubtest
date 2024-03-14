#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 05:49:11 2023

@author: user
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

df = pd.read_csv(r'/Users/user/Desktop/insurance.csv')

#練習17
#去除用不到的非數值欄位
df = df.drop(['Gender','Vehicle_Damage', 'Vehicle_Age'], axis=1)
# 計算年齡平均(以是否擁有車險分類)
age_mean = df.groupby("Previously_Insured", as_index=False).mean()
# 長條圖繪製
sns.barplot(x="Previously_Insured", y="Age", data=age_mean)
#在長條圖上方加上實際數值標示
ax = sns.barplot(x="Previously_Insured", y="Age", data=age_mean)
for index, row in age_mean.iterrows():
    ax.text(index, row.Age, row.Age, ha="center", va="bottom")
#加入門檻識別線
ax = sns.barplot(x="Previously_Insured", y="Age", data=age_mean)
ax.axhline(30, color="red")



# #練習18
# #去除沒用到的非數值欄位，下面的分組才能順利跑
# df = df.drop(['Gender', 'Vehicle_Damage'], axis=1)
# # 以車齡分組計算各組每欄位平均
# df_mean = df.groupby("Vehicle_Age", as_index=False).mean()
# # 只保留想用的欄位，設定新的dataframe (df2)
# df2 = df_mean[['Vehicle_Age','Previously_Insured','Response']]
# # 調整資料框架的格式
# # The .stack() method in pandas is used to pivot a DataFrame from a wide format to a long format. It takes columns and pivots them into rows, converting the DataFrame into a Series with a MultiIndex.
# # The .rename_axis() method is used to rename the labels of the index or columns of a DataFrame. It's helpful for assigning a name to the index or columns, making the DataFrame more descriptive and aiding readability.
# # The .reset_index() method is used to reset the index of a DataFrame. It converts the index (which might be a multi-level index) into a column and creates a default numbered index. This operation allows you to turn index labels into regular columns.
# # The .rename(columns={}) method is used to rename columns in a DataFrame by passing a dictionary where keys are the old column names and values are the new column names. This is useful when you want to change column names selectively or comprehensively throughout the DataFrame.
# df2 = df2.set_index("Vehicle_Age")
# df2 = df2.stack().rename_axis(["Vehicle_Age", "type"]).reset_index().rename(columns={0: "平均傾向"})

# #練習19
# sns.barplot(x="Vehicle_Age", y="平均傾向", hue="type", data=df2)

# #練習20
# #plotly 長條圖
# df_mean = df.groupby("Vehicle_Age", as_index=False).mean()
# fig = go.Figure(data=[go.Bar(name="Previously_Insured", 
#                               x=df_mean["Vehicle_Age"],
#                               y=df_mean["Previously_Insured"]),
#                       go.Bar(name="Response", 
#                               x=df_mean["Vehicle_Age"],
#                               y=df_mean["Response"])])
# # 排列長條圖
# fig.update_layout(barmode="group")
# fig.show()

