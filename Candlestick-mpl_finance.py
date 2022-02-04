import matplotlib.pyplot as fig
import datetime as dt
import mpl_finance as mpf
import matplotlib.dates as mdates
import pandas_datareader.data as web

inicio=dt.datetime(2019,1,1)
fim=dt.datetime(2022,2,2)
df=web.DataReader('MGLU3.SA','yahoo',inicio,fim)

df['med_mov']=df['Close'].rolling(window=20,min_periods=0).mean()
df_ohlc=df['Close'].resample('7D').ohlc()
df_ohlc['Volume']=df['Volume'].resample('7D').sum()

df_ohlc.reset_index(inplace=True)
df_ohlc['Date']=df_ohlc['Date'].map(mdates.date2num)

ax1=fig.subplot(211)
ax1.xaxis_date()
mpf.candlestick_ohlc(ax1,df_ohlc.values,width=2,colorup='g')
ax1.plot(df.index,df['med_mov'])