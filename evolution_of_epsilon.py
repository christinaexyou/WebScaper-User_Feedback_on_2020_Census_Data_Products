#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 09:42:08 2022

@author: christinaxu
"""

import plotly.graph_objects as go
from plotly.offline import init_notebook_mode, plot
init_notebook_mode(connected=True)
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np
import datetime

df=pd.DataFrame({'Date': ['Nov 2018','Oct 2019','May 2020','Sep 2020','Nov 2020','Apr 2021', 'Apr 2021','Jun 2021'], 
                 'DP': ['Pure', 'Pure', 'Pure', 'zCDP', 'zCDP','zCDP', 'zCDP', 'zCDP'],
                 'PL-Epsilon': [0.25,6.0,4.5,4.5,4.5,4.5,12.2,19.61],
                 'Effective TPR': [	0.01285, 0.9976,0.90018,0.90018,0.90018,
                                   0.90018, 0.9999955,0.999999997]})

df['Date'] = pd.to_datetime(df['Date'])
df['Date'] = df['Date'].dt.strftime('%Y-%m')
print(df['Date'])
DP = np.unique(df['DP'].values)
DP_as_numbers = dict(zip(DP, np.arange(len(DP))))
print(DP_as_numbers)

def SetColor(x):
    if x =='Pure':
        return 'aquamarine'
    else:
        return 'salmon'

fig = make_subplots(
    rows=2, cols=1,
    subplot_titles=('Evolution of PL Privacy Loss Budget ', 'Effective TPR vs. PL-Epsilon')) 
  
# PL-Epsilon vs. Date       
fig.add_trace(
    go.Scatter(x=df['Date'], y=df['PL-Epsilon'],
    mode='markers + text', 
    marker = dict(color=list(map(SetColor,df['DP']))),
    text = df['PL-Epsilon'],
    textposition = 'bottom center',
    hovertemplate = ['Choice of epsilon <br> was exclusive to  <br> this demonstration and <br> do not extend to <br> the 2020 Census', 
                     'Privacy loss budget <br> was used to produce a <br> limited set of data <br> products and did not <br> reflect the global privacy <br> loss budget for <br> the 2020 Census', 
                     'Purposefully tuned to <br> privacy and not <br> tuned to accuracy', 
                     'Change from Pure-DP to <br> zCDP based on feedback <br> from data users concerned <br> about the occurance of significant <br> outliers in earlier demonstration <br> data products',
                     'N/A',
                     'Included for comparisons <br> for previous demonstration <br> data releases to reflect <br> improvements in the TopDown algorithm <br> and post-processing' ,
                     'Minimal improvements <br> in accuracy compared <br> to epsilon = 4.5. <br> Although errors in the <br> total population <br> were mitigated <br> major errors persisted <br> in smaller populations',
                     'Data users identified a <br> need for more accuracy <br> in race and ethnicity statistics <br> at various levels of geography; <br> place, Minor Civil Division, and <br> tract levels; occupanct rates <br> at th block group and <br> levels of higher geography'],
    hoverinfo = 'text',
    line=dict(color='#CCCCFF'), showlegend = False),
    row=1, col=1)

# Effective TPR vs. PL-Epsilon
fig.add_trace(
    go.Scatter(x=df["PL-Epsilon"], y=df['Effective TPR'], 
    mode='markers',
    hovertemplate= 'Epsilon: %{x} <br>TPR: %{y}<extra></extra>',
    line=dict(color='#98ffcc'), showlegend=False), 
    row=2, col=1)

fig.update_xaxes(title_text='Date', row=1, col=1)
fig.update_xaxes(title_text='PL-Epsilon',row=2, col=1)

fig.update_yaxes(title_text='PL-Epsilon',row=1,col=1)
fig.update_yaxes(title_text='Effective TPR',range=[0,1.5],row=2,col=1)

fig.update_layout(height=900,width=800, template='plotly_dark')

plot(fig)


