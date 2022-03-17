# 定位、旋转数据表（行/列转换）


import pandas as pd 

# 设置最大显示列数为20
pd.options.display.max_columns=20
video = pd.read_excel('./Videos.xlsx',index_col='Month')
print('----原始数据----')
print(video)
print(video.columns)

table = video.transpose()
print('\n----行列转换的结果----')
print(table)