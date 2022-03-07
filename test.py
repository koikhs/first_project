import finterstellar as fs
import FinanceDataReader as fdr
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# df = fdr.DataReader('048260', '2021')
# print(df)
# df.tail()
#
# ma5 = df['Close'].rolling(window=5).mean()
# df['ma5'] = ma5
# df.tail()
#
# ma20 = df['Close'].rolling(window=20).mean()
# df['ma20'] = ma20
#
# ma60 = df['Close'].rolling(window=60).mean()
# df['ma60'] = ma60
#
# ma120 = df['Close'].rolling(window=120).mean()
# df['ma120'] = ma120
#
# def draw(df):
#   plt.figure(figsize=(10, 5))
#   plt.plot(df.index, df['Close'],label='Close')
#   plt.plot(df.index, df['ma5'],label='ma5')
#   plt.plot(df.index, df['ma20'],label='ma20')
#   plt.plot(df.index, df['ma60'],label='ma60')
#   plt.plot(df.index, df['ma120'],label='ma120')
#
#   plt.legend()
#   plt.grid(alpha=0.5)
#   plt.show()
#
# draw(df.loc['2019':])



df = fs.get_price('AAPL', start_date='2020-11-20', end_date='2021-11-20')
print(df)

fs.rsi(df, w = 14)
fs.draw_chart(df, left='rsi', right='AAPL')
fs.macd(df)

fs.draw_chart(df,right=['macd','macd_signal','macd_oscillator'])
#
#
# def get_data(stock,start,end):
#   df = fs.get_price(stock,start_date=start,end_date=end)
#   fs.draw_chart(df,right=stock)
#   return df
#
# df = get_data('SBUX','2020-01-01','2021-10-23')
# print(df)


# print("Hello World!")
# print("안녕하세요")

