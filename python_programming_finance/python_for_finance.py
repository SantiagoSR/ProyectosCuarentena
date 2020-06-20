import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import  mplfinance 
import matplotlib.dates as mdates


import pandas as pd
from pandas_datareader import data as web



style.use('ggplot')

##start = dt.datetime(2000,1,1)
##end = dt.datetime(2019,12,31)

##df = web.DataReader('TSLA','yahoo',start,end)
##df.to_csv('tsla.csv')

df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0)

##df['Adj Close'].plot() para solo mostrar una columna
##plt.show()

##revisar esto de 100 ma: conocer mas acerca de este
##df['100ma'] = df['Adj Close'].rolling(window=100,min_periods=0).mean()

##reads open/high/low/close of the 10 days
df_ohlc = df['Adj Close'].resample('10D').ohlc()
df_volume = df['Volume'].resample('10D').sum()

df_ohlc.reset_index(inplace=True)

df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)



ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)

ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1,sharex=ax1)

##ax1.xasxis_date()
kwargs = dict(type='candle', mav=(2,4,5), volume= True, figratio=(11,8), figscale=0.85)
mplfinance.plot(df, **kwargs,style='charles')

##graficas

##ax1.plot(df.index, df['Adj Close'])

##ax1.plot(df.index, df['100ma'])

##ax2.bar(df.index, df['Volume'])


##plt.show()
