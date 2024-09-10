import matplotlib.pyplot as plt
import mplfinance as mpf
import yfinance as yf
import time

while True:
    # Download historical data from Yahoo Finance
    data = yf.download("EURUSD=X", period="30m", interval="5m")

    # Plotting with autoscaling and zooming
    mpf.plot(data, type='candle', style='charles', volume=True, tight_layout=True)

    # Show the plot
    plt.show()

    # Wait for 1 minute
    #time.sleep(60)
