import matplotlib.animation as ani
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv'
df = pd.read_csv(url, delimiter=',', header='infer')
print(df.head())

df2 = df.set_index('date')
df2 = df.reset_index().groupby(['date', 'state'])['cases'].aggregate('first').unstack()
df2.fillna(0)
df3 = df2[['New York', 'California', 'Texas', 'Florida']]
df3.index = pd.to_datetime(df3.index)
print(df3.head().fillna(0))
print(df3.index)

fig = plt.figure()
bar = 'vertical'    #leave this blank for horizontal graph
def buildmebarchart(i=int):
    iv = min(i, len(df3.index)-1)
    objects = df3.max().index
    y_pos = np.arange(len(objects))
    performance = df3.iloc[[iv]].values.tolist()[0]
    if bar == 'vertical':
        plt.bar(y_pos, performance, align='center', color=['red', 'green', 'blue', 'orange'])
        plt.xticks(y_pos, objects)
        plt.ylabel('Cases')
        plt.xlabel('States')
        plt.title('Cases per State \n' + str(df3.index[iv].strftime('%y-%m-%d')))
    else:
        plt.barh(y_pos, performance, align='center', color=['red', 'green', 'blue', 'orange'])
        plt.yticks(y_pos, objects)
        plt.xlabel('Cases')
        plt.ylabel('States')
        plt.title('Cases per State \n' + str(df3.index[iv].strftime('%y-%m-%d')))

animator = ani.FuncAnimation(fig, buildmebarchart, interval=500)
plt.show()