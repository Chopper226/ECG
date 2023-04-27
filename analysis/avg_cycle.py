# 分割每段數據，並繪圖

import plotly.graph_objects as go
import numpy as np
import pandas as pd
from scipy.signal import find_peaks

data = np.array( pd.read_csv('Data\\30605\\平躺.txt') )
data = data[0 :,0] # 選取需要的數值範圍

peak_list = find_peaks( data , height = 80 , distance = 250 )[0]  # 每一下心跳的波鋒之時間
peak = np.zeros((len( peak_list )-1,394), dtype=int) # 建立存放擷取週期數值的陣列
data = data.tolist() # float64 -> float
peak_list = peak_list.tolist()


for i in range( 0 , len( peak_list )-1 ) :
    k=0
    for j in range ( peak_list[i]-197 , peak_list[i]+197 ) :
        num = int(data[j])
        peak[i][k] = num
        k+=1
        
peak = np.mean( peak , axis=0 )

fig = go.Figure()
fig.add_trace( go.Scatter ( y = peak, name = '心電訊號' ) )

fig.update_layout(
    title="在躺著狀態下，每個周期的總圖", 
    font=dict(
        family = "Courier New, monospace" , size = 20 , color = "RebeccaPurple"
    )
)

fig.show()