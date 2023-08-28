import json
import websocket
import pickle
import sys
import os
import datetime
import pandas as pd

MAX_LENGTH = 200
df = {}  # Initialize an empty dictionary to store data

def on_open(self):
    print("Open connection with binance.com")
    subscribe_message = {
        "method": "SUBSCRIBE",
        "params": ["btcusdt@depth@100ms"],
        "id": 1
    }
    ws.send(json.dumps(subscribe_message))

def save_dictionary(dictionary, filename):
    with open(filename, 'ab') as file:
        pickle.dump(dictionary, file)

def on_message(self, message):
    orderbook = json.loads(message)

    if len(df) > MAX_LENGTH:
        print('Deleting...', list(df.keys())[0])
        del df[list(df.keys())[0]]

    print(len(df))

    if 'b' in orderbook.keys() or 'a' in orderbook.keys():
        prices_bids = [entry[0] for entry in orderbook['b']]
        quantities_bids = [entry[1] for entry in orderbook['b']]

        df[orderbook['u']] = {'bids': orderbook['b'], 'asks': orderbook['a']}
        save_database(df, filepath_orderbook)

def save_database(database, filename):
    with open(filename, 'wb') as file:
        pickle.dump(database, file)

def on_close(self):
    print("Closed connection")

if __name__ == "__main__":
    symbol = 'btcusdt'
    counter = 0
    initial_filepath_orderbook = sys.path[0] + f'/orderbook_{symbol}_{counter}_{str(datetime.datetime.now())[:10]}.pkl'
    filepath_orderbook = initial_filepath_orderbook

    if os.path.exists(filepath_orderbook):
        counter += 1
        filepath_orderbook = filepath_orderbook

    socket = 'wss://stream.binance.com:9443/ws'
    ws = websocket.WebSocketApp(socket,
                                on_open=on_open,
                                on_message=on_message,
                                on_close=on_close)
    ws.run_forever()

