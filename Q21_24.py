#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 09:33:15 2023

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

#練習21
#去除沒用到的非數值欄位，下面的分組才能順利跑
df = df.drop(['Gender', 'Vehicle_Damage'], axis=1)
# 以車齡分組計算各組每欄位平均
df_mean = df.groupby("Vehicle_Age", as_index=False).mean()
# 只保留想用的欄位，設定新的dataframe (df2)
df2 = df_mean[['Vehicle_Age','Previously_Insured','Response']]
df2 = df2.set_index("Vehicle_Age")
df2 = df2.stack().rename_axis(["Vehicle_Age", "type"]).reset_index().rename(columns={0: "平均傾向"})
ax = sns.barplot(x="Vehicle_Age", y="平均傾向", hue="type", data=df2)
# 於右上角顯示圖例
ax.legend(loc="upper left", bbox_to_anchor=(1, 1))
# # 於右下角顯示圖例 
# ax.legend(loc="lower left", bbox_to_anchor=(1, 0))
# # 於圖表正下方顯示圖例
# ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.15))


#練習22
#去除用不到的非數值欄位
df = df.drop(['Gender','Vehicle_Damage'], axis=1)
# 計算每種車齡下的平均
means = df.groupby("Vehicle_Age", as_index=False).mean()
# 設定顏色
default_color = "#555555"  # 標準色
point_color = "#CC0000"  # 重點色
idx = 2 # 要突顯的長條
# 建立調色盤
palette = sns.color_palette([default_color], len(means))
palette[idx] = sns.color_palette([point_color])[0]
#產生每種車齡下的年齡平均
sns.barplot(x="Vehicle_Age", y="Age", data=means, palette=palette)


#練習23
#去除用不到的非數值欄位
df = df.drop(['Gender','Vehicle_Damage'], axis=1)
# 計算每種車齡下的平均
means = df.groupby("Vehicle_Age", as_index=False).mean()
sns.barplot(x="Vehicle_Age", y="Annual_Premium", data=means)


#練習24
#去除用不到的非數值欄位
df = df.drop(['Gender','Vehicle_Damage'], axis=1)
# 計算每種車齡下的平均
means = df.groupby("Response", as_index=False).mean()
f, axs = plt.subplots(1, 2)
#ax=axs[0]代表圖會被畫在第一個子圖
sns.barplot(x="Response", y="Annual_Premium", ax=axs[0], data=means)
sns.barplot(x="Response", y="Vintage", ax=axs[1], data=means)
plt.savefig("combined bar.png", dpi=900)




