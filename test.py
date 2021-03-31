import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

print('Hello World')
# This is a comment

# Example with Microsoft


msft = yf.Ticker("MSFT")
df_msft = msft.history(period="1y")
print(df_msft)
rm_msft = df_msft['Open'].rolling(20).mean()
rstd_msft = df_msft['Open'].rolling(20).std()

df_msft['Open'].plot()
rm_msft.plot(label = 'mean')
(rm_msft-2*rstd_msft).plot(label = 'mean-2std')
(rm_msft+2*rstd_msft).plot(label = 'mean+2std')
plt.legend()
plt.show()