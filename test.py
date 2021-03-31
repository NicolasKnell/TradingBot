import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

print('Hello World')
# This is a comment

# Example with Microsoft


msft = yf.Ticker("MSFT")
df_msft = msft.history(period="6mo")
df_msft.to_csv('MSFT.csv')
print(df_msft)
rm_msft = df_msft['Open'].rolling(5).mean()
rstd_msft = df_msft['Open'].rolling(5).std()
daily_returns = (df_msft['Open']/df_msft['Open'].shift(1)) - 1
print(daily_returns)

fig, ax = plt.subplots(2, constrained_layout=True)

ax[0].plot(df_msft['Open'], label = 'Stock Price')
ax[0].plot(rm_msft, label = 'mean')
ax[0].plot((rm_msft-2*rstd_msft), label = 'mean-2std')
ax[0].plot((rm_msft+2*rstd_msft),label = 'mean+2std')
ax[0].grid(True)
ax[0].legend(loc = 'lower right')
ax[0].tick_params('x', labelrotation=30)
ax[0].set_title('Stock Price Variation')

ax[1].plot(daily_returns, label = 'daily_returns')
ax[1].tick_params('x', labelrotation=30)
ax[1].legend(loc = 'lower right')
ax[1].grid(True)
ax[1].set_title('Stock Daily Return Variation')

plt.show()


