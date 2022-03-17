# 读取文件


import pandas as pd

# --基本数据的读取--

# 读取文件
# header:指定数据表头，默认0，将第一行作为表头
# index_col: 指定数据的索引列
people = pd.read_excel('./People.xlsx',header=0,index_col='ID')
# print(people)
# 读取文件的行数和列数
shape = people.shape
# print(shape)
# 读取文件的行,不会显示索引列
columns = people.columns
# print(columns)
# 读取文件的前几行（默认为5，可传入指定行数）
head = people.head()
# print(head)
# 读取文件的末尾几行（默认为5，可传入指定行数）
tail = people.tail()
# print(tail)

