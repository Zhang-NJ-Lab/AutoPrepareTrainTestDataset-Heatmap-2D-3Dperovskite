# AutoPrepareTrainTestDataset-Heatmap-2D-3Dperovskite
AutoPrepareTrainTestDataset and prepare Heatmap for 2D-3D perovskite dataset

## 文件描述
v2-bianliwenjian.sh   linux文本自动读取dmol3里的.outmol Eg, VBM, CBM， 生成Eg.csv    CBM.csv    VBM.csv


Eg1.csv 不含输出的材料元素成分名称（加入行索引）


Periodic Talbe of Elements.csv 元素原始描述符汇总


## 需要用2_perovskite.py 自动生成元素的描述符，需要用到Eg1.csv和Periodic Talbe of Elements.csv

## 生成了Eg_final.csv文件，然后手动删除前几列并添加t,u形成Eg_final2.csv

## ML文件夹生成了热图，需要用用Eg_final2.csv
