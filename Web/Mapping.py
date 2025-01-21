# Read data from excel file and convert to python dictionary

import pandas as pd
import numpy as np
import os

def create_map(name):
    file_path = "static/database/" + name 

    df = pd.read_csv(file_path, header=None)

    df = df.set_index(0)[1].to_dict()

    new_dict = {}

    for key, value in df.items():
        new_dict[str(key)] = value

    return new_dict








