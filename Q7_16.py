#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 05:40:59 2023

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

#練習7
sns.scatterplot(x="Annual_Premium", y="Vintage", data=df)
# sns.scatterplot(x="Annual_Premium", y="Vintage", hue="Previously_Insured", data=df)

#練習8
sns.scatterplot(x="Annual_Premium", y="Vintage", style="Response", data=df)
# sns.scatterplot(x="Annual_Premium", y="Vintage", hue="Response", alpha=0.5, data=df)

#練習9
ax = sns.scatterplot(x="Age", y="Annual_Premium", hue="Vehicle_Damage", size="Vintage",
                      data=df, sizes=(10, 200)) 
ax.legend(loc="upper left", bbox_to_anchor=(1, 1))

#練習10
fig = px.scatter(df, x="Age", y="Annual_Premium", size="Vintage", color="Response",
                  size_max=50) 
fig.show()

#練習11
sns.pairplot(data=df)
# sns.pairplot(data=df, hue="Response")
plt.savefig("/Users/user/Desktop/pairplot.png", dpi=900)

#練習12
sns.jointplot(x="Annual_Premium", y="Age", data=df)

#練習13
sns.jointplot(x="Annual_Premium", y="Age", color="r", data=df)
sns.jointplot(x="Annual_Premium", y="Age", kind="hex", data=df)

#練習14
sns.catplot(x="Response", y="Annual_Premium", hue="Previously_Insured", data=df)

#練習15
fig = px.parallel_coordinates(df, dimensions=["Region_Code", "Annual_Premium", "Response"])
fig.show()

#練習16
fig = px.parallel_categories(df)
fig.show()

