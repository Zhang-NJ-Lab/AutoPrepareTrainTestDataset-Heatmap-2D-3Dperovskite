
# 程序说明：
# 从一个csv文件里提取内容到另一个csv文件，填充到特定位置
# 核心实现：
# pandas的精确定位pandas.loc[index,columns];
# if判断确定行索引；
# 嵌套的for循环实现批量化
# 难点问题：
# 将空值的NAN填充为0以实现数据转换；
# 修改源数据使用inplace=True参数；也可利用赋值改变源数据；
# 对快照进行源数据修改，源数据会被修改；可多次读取同一个文件，这样即使修改一个源数据，其它文件不受影响(程序中Ion列的替换);
# 对使用正则过滤后的多列数据进行整体赋值以修改源数据(类型)***


import pandas as pd
import numpy as np

# from pandarallel import pandarallel
# pandarallel.initialize()  #导入并行模块，初始化后就可以用，适用于linux mac

df1 = pd.read_csv("Eg1.csv", encoding_errors='ignore')
df2 = pd.read_csv("Periodic Table of Elements.csv", encoding_errors='ignore')
df3 = pd.read_csv('Eg1.csv', encoding_errors='ignore')
df1_copy = df1
df2_copy = df2
df2_copy.index[1]
df1_copy.replace(np.nan, 0, inplace=True)  # 把nan或inf填充为0，这样才能进行数据转换

# ls1=df1_copy.columns[2:10]#['A1', 'A2', 'B', 'X1', 'X2', 'X3', 'X4','Ion']

# python range(2,10)表示不包括10但包括2; pandas[2:10]也是不包括10
ls = ['NumberofProtons', 'NumberofNeutrons', 'NumberofShells', 'SpecificHeat',
      'Density', 'Ion Radius', 'FirstIonization', 'AtomicMass', 'MeltingPoint']
# ls1=['Li','Zn','K','Na','Al','Ca','Mg','F',]

# df1_copy.Ion.replace('[0-9\+\-]','',regex=True,inplace=True)
for k in df1_copy.index:
    for j in range(1, 7):
        #         print(df1_copy.columns[j])
        for i in df2_copy.index:
            if df2_copy.Symbol[i] == df1_copy[df1_copy.columns[j]][k]:
                for l in ls:
                    str1 = df1_copy.columns[j] + ' ' + l
                    #                     print('*'*100)
                    #                     print(str1)
                    df1_copy.loc[k, str1] = df2_copy.loc[i, l]

df1_copy.filter(regex='Number') # 把所有含number的列数据类型设置为整数

# # 想要真正的改变数据框，通常需要通过赋值来进行，比如
# df["Customer Number"] = df["Customer Number"].astype("int")
df1_copy[df1_copy.filter(regex='Number').columns] = df1_copy.filter(regex='Number')
# df1_copy.Ion=df3.Ion

df1_copy.to_csv('Eg_final.csv')
