import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
from pandas_datareader import data as web

style.use('ggplot')

start = dt.datetime(2000,1,1)
end = dt.datetime(2019,12,31)

df = web.DataReader('TSLA','yahoo',start,end)

df['Adj Close'].plot()
plt.show()