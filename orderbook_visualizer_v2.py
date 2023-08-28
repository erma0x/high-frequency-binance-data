import time
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

def sum_arrays(arr1, arr2):
    # Create a defaultdict to store the keys and summed values
    result_dict = defaultdict(int)

    # Iterate over the first array
    for key, value in arr1:
        # Sum the values
        result_dict[key] += value

    # Iterate over the second array
    for key, value in arr2:
        # Sum the values
        result_dict[key] += value

    # Convert the dictionary back to a numpy array
    result_array = np.array([[key, value] for key, value in result_dict.items()])

    return result_array


def get_price_and_quantities(df, side='bids'):
    full_data = []

    for key in df.keys():
        print(key)
        value = df[key][side]
        string_list = str(value)
        list_of_lists = eval(string_list)

        # Append the list of lists to the full_data list
        full_data.extend(list_of_lists)

    # Convert the full_data list to a numpy array with dtype=float
    full_data_array = np.array(full_data, dtype=float)

    # Sum the quantities based on the prices
    unique_prices, quantities = np.unique(full_data_array[:, 0], return_counts=True)

    return unique_prices, quantities
    
    
def update_plot():
    # Get the latest prices and quantities
    prices, quantities = get_price_and_quantities(df)

    # Clear the current plot
    plt.cla()

    # Create a horizontal bar plot
    plt.barh(range(len(prices)), quantities, tick_label=prices)

    # Set the labels and title
    plt.xlabel('Quantity')
    plt.ylabel('Price')
    plt.title('Bitcoin USDT Orderbook')

    # Redraw the plot
    plt.draw()

# Read the data from the pickle file
df = pd.read_pickle('orderbook_btcusdt_0_2023-08-17.pkl')

# Set the initial plot
update_plot()

# Continuously update and display the plot every 0.1 seconds
while True:
    df = pd.read_pickle('orderbook_btcusdt_0_2023-08-17.pkl')

    # Wait for 0.1 seconds
    time.sleep(0.1)

    # Update and display the plot
    update_plot()




