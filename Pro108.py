import csv
import pandas as pd
import plotly.figure_factory as pff

df=pd.read_csv('mobile_data.csv')
avgrating=df['Avg Rating'].tolist()

graph=pff.create_distplot([avgrating],["Avg Rating"],show_hist=False)
graph.show()