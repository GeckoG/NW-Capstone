'''
This is a machine learning model that predicts the future top-100 average of track and field events.
Created on Monday, April 1st, 2024
Author: Matt Goeckel
'''
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the data
df = pd.read_csv('top100avg.csv')

