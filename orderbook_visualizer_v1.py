import pickle
import time
import os
import pandas as pd
import matplotlib.pyplot as plt

# Function to read objects from a pickle file
def read_objects_from_pickle(filepath):
    try:
        with open(filepath, 'rb') as file:
            objects = []
            while True:
                try:
                    obj = pickle.load(file)
                    objects.append(obj)
                except EOFError:
                    break
            return objects
    except FileNotFoundError:
        print("File not found.")
    except pickle.UnpicklingError as e:
        print(f"Error: Failed to unpickle object. Reason: {str(e)}")

# Function to save dictionaries to a pickle file
def save_dictionaries(dictionaries, filename):
    with open(filename, 'ab') as file:
        pickle.dump(dictionaries, file)

# Function to delete the oldest elements from a pickle file
def delete_oldest_elements(filepath, max_length):
    if not os.path.exists(filepath):
        print(f"File '{filepath}' does not exist.")
        return
    
    objects = read_objects_from_pickle(filepath=filepath)
    
    if len(objects) > max_length:
        objects_to_save = read_objects_from_pickle(filepath)
        # del objects_to_save[0]
        save_dictionaries(objects_to_save, filepath)

# Main program
if __name__ == "__main__":
    
    while True:
    
        filepath_orderbook = 'orderbook_btcusdt_0_2023-08-17.pickle'
        MAX_LENGTH = 25

        obj = read_objects_from_pickle(filepath_orderbook)
        
        if obj:
            print(len(obj))
            if len(obj) > MAX_LENGTH-1:
                delete_oldest_elements(filepath_orderbook, max_length=MAX_LENGTH)

        time.sleep(0.1)

