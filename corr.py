import ssl
import os
import pandas as pd
import glob
import csv
import re
import numpy as np
import datetime as dt
from pandas.core.indexes.base import Index

codelist=['9983','7751','5201','2871','9613','6752','4507','2809','8411','5332','3407','2296']
path="stock_data\\"
df1 = pd.read_csv(path + "stockopencode.csv",encoding="cp932")

df1['date'] = pd.to_datetime(df1['date'])
df5 = df1[df1['date']>dt.datetime(2018,7,1)]
for code in codelist:
    print(code)
    if not code in df1.columns:
        continue
    colist = []
    df2 = df5[code]
    df2 = df2.reset_index(drop = True)
    length = len(df2)
    length = length - 1
    for s in df1.columns[3::]:
        df3 = df1.loc[0:length,s]

        df4 = pd.concat([df2,df3],axis=1)
        df4.columns = ['1','2']
        df4 = df4[(df4["1"] != 0 ) & (df4['2'] != 0) ]
        corr = df4.corr()
        colist.append(corr.loc['1','2'])
    colist_sort=sorted(colist,reverse=True)
    print(colist_sort[0:5])
    indexlist = []
    for i in colist_sort[0:5]:
        indexnum = colist.index(i)
        indexlist.append(indexnum+3)
    print(df1.columns[indexlist])