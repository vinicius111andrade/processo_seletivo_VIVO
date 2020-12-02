from flask import Flask
from flask import request
import json
import numpy as np
import pandas as pd

df = pd.read_csv("log_corrida.csv") 
print(df.head()) 