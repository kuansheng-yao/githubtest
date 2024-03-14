#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 05:33:27 2023

@author: user
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import plotly.offline
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots
import squarify

df = pd.read_csv(r'/Users/user/Desktop/insurance.csv')

#練習1
plot1 = sns.distplot(df["Age"], kde=False)
# plot2 =sns.distplot(df["Age"], kde=False, bins=15)
# plot3 =sns.distplot(df["Age"], vertical=True, kde=False)

#練習２
over_2 = df[df["Vehicle_Age"] == "> 2 Years"]
one_two = df[df["Vehicle_Age"] == "1-2 Year"]
under_1 = df[df["Vehicle_Age"] == "< 1 Year"]
sns.distplot(over_2["Vintage"], kde=False, bins=20, color="red")
sns.distplot(one_two["Vintage"], kde=False, bins=20, color="blue")
sns.distplot(under_1["Vintage"], kde=False, bins=20, color="green")

#練習3
sns.countplot(x="Response", data=df)

#練習4
sns.countplot(x="Response", hue="Vehicle_Age", data=df)

#練習5
sns.boxplot(y="Vintage", data=df)
# sns.boxplot(x="Vehicle_Age", y="Age", data=df)

#練習6
# sns.boxplot(x="Vehicle_Age", y="Age", order=[,,,], data=df)
sns.boxplot(x="Vehicle_Age", y="Annual_Premium", hue="Response", data=df)
