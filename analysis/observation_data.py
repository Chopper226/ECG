# 觀察數據

import plotly.graph_objects as go
import numpy as np
import pandas as pd
from scipy.signal import find_peaks

df = pd.read_csv('Data\\30605\\平躺.txt')
data = np.array(df)
data2 = data[0:,0]

fig = go.Figure()
fig.add_trace( go.Scatter ( y = data2 , name = 'Original Plot' ) )
fig.update_layout(
    title="心電訊號",
    font=dict( family = "Courier New, monospace", size = 20 , color = "RebeccaPurple" )
)
fig.show() 