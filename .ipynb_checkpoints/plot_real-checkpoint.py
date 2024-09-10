import matplotlib.pyplot as plt
import mplfinance as mpf
import yfinance as yf
import time

# Create figure and subplot
fig, ax = plt.subplots()

# Initialize empty lists to store x and y data
data = yf.download("EURUSD=X", period="30m", interval="5m")

# Function to update plot with new data
def update(data):
    ax.clear()
    mpf.plot(data, type='candle', style='charles', volume=False, tight_layout=True, ax=ax)
    plt.pause(0.01)

# Show the initial plot
update(data)
plt.show(block=False)

while True:
    # Download historical data from Yahoo Finance
    data = yf.download("EURUSD=X", period="30m", interval="5m")

    # Update the plot
    update(data)

    # Wait for 1 minute
    time.sleep(2)