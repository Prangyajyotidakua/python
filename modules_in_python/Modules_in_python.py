import math
print(math.sqrt(16))  # Calculates the square root of 16

from math import pi  # Import the 'pi' constant
print('value of pi is ' + str(pi))

import random
print(random.randint(1, 10))  # Generates a random integer between 1 and 10

import datetime
current_time = datetime.datetime.now()
print(current_time)

import os
print(os.getcwd())  # Get the current working directory

import sqlite3
conn = sqlite3.connect('mydb.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE users (id INT, name TEXT)')
conn.commit()

import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)
print(df)

import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [10, 15, 7, 12, 9]
plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Plot')
plt.show()

import numpy as np
array = np.array([1, 2, 3, 4, 5])
print(np.mean(array))  # Calculates the mean of the array

import requests
response = requests.get('https://www.example.com')
print(response.status_code)
