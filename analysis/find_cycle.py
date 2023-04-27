import plotly.graph_objects as go
import numpy as np
import pandas as pd
from scipy.signal import find_peaks

df = pd.read_csv('Data\\30605\\平躺.txt')
data = np.array(df)
data2 = data[0:,0] # 更改選取的資料範圍

peak_list = find_peaks( data2 , height = 80 , distance = 250 )[0]  # 每一下心跳的波鋒之時間
        
peak_time = np.diff( peak_list ) # 每下心跳間隔時間
print( 'peak_time : ',peak_time )
print( 'avg : ',np.mean( peak_time ) )