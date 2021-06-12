import random
import statistics as stats
import csv
import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px
import plotly.graph_objects as go

df=pd.read_csv("data/data.csv")
data=df["average"].tolist()
dataset=[]

mean_pop=stats.mean(data)
std_dev_pop=stats.stdev(data)

for i in range(0,1000):
  value=random.randint(0,len(data)-1)
  dataset.append(data[value])

mean_100=stats.mean(dataset)
std_dev_100=stats.stdev(dataset)


fig=ff.create_distplot([dataset],["value"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean_100,mean_100], y=[0, 2], mode="lines", name="MEAN"))
fig.show()


print('Mean of 1000 : ',mean_100)
print('Standard deviation of 1000 : ',std_dev_100)

print('Mean of population : ',mean_pop)
print('Standard deviation of population : ',std_dev_pop)


