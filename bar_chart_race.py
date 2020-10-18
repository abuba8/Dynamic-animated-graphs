#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import bar_chart_race as bcr
import numpy as np
import cv2

df = pd.read_csv("https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv")
print(df.head())

df2 = df.set_index('date')
df2 = df.reset_index().groupby(['date','state'])['cases'].aggregate('first').unstack()
df2.fillna(0)

df3 = df2[['New York','California','Texas','Florida']]
bcr.bar_chart_race(df3.fillna(0), filename="xyz.mp4", title = "Covid in US States")


cap = cv2.VideoCapture('xyz.mp4')

while(cap.isOpened()):
    ret, frame = cap.read()
    
    if ret == True:
        cv2.imshow('COVID', frame)
        
        if cv2.waitKey(25) == ord('q'):
            break
        
    else:
        break

cap.release()
cv2.destroyAllWindows()