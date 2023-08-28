# WebSocket Data Collection with Python

This Python script collects real-time order book data from the Binance cryptocurrency exchange using WebSocket communication. The collected data is stored in a dictionary and saved to a file using the pickle module.


## Code Overview

The code consists of the following main components:

- Importing the necessary libraries: json, websocket, pickle, sys, os, datetime, and pandas.
- Defining a constant variable MAX_LENGTH.
- Initializing an empty dictionary df to store the order book data.
- Defining the on_open, save_dictionary, on_message, save_database, and on_close functions.
- The main section that establishes a WebSocket connection and runs the program.


## Code Explanation

- The `on_open` function is called when the WebSocket connection is established. It sends a subscription message to the Binance API to receive order book data for the BTC/USDT trading pair.
- The `save_dictionary` function saves the dictionary to a file using the pickle module.
- The `on_message` function is called whenever a new message is received from the WebSocket connection. It processes the order book data, updates the dictionary, and saves it to a file if necessary.
- The `save_database` function saves the entire database (dictionary) to a file using the pickle module.
- The `on_close` function is called when the WebSocket connection is closed.
- The main section of the code initializes variables, checks if a file with the same name already exists, establishes the WebSocket connection, and runs the program indefinitely.


## Usage

1. Install the required libraries by running the following command:
`pip install websocket-client pandas`


2. Replace the `filepath_orderbook` variable with the desired file path for storing the order book data.

3. Run the script using the following command:
`python bot.py`

4. The script will establish a WebSocket connection with Binance and start collecting order book data. The data will be stored in the specified file path.

5. To stop the script, press `Ctrl + C`.


## Requirements

- Python 3.x
- websocket-client
- pandas


## Conclusion

This Python script provides a simple way to collect real-time order book data from Binance using WebSocket communication. Feel free to modify and customize the code according to your needs.

If you have any questions or suggestions, please feel free to reach out.



