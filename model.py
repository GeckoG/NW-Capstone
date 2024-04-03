'''
This is a machine learning model that predicts the future top-100 average of track and field events.
Created on Monday, April 1st, 2024
Author: Matt Goeckel
'''
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load the data
df = pd.read_csv('top100avg.csv')

# Preprocess the data
le = LabelEncoder()
df['Division'] = le.fit_transform(df['Division'])
df['Sex'] = le.fit_transform(df['Sex'])
df['Event'] = le.fit_transform(df['Event'])

# Split the data into features and target
X = df.iloc[:, :14]  # columns 1-3 and 4-14 (2010-2022)
y = df.iloc[:, 14]  # actual 2023 values

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Choose a model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
print('RMSE:', mean_squared_error(y_test, y_pred, squared=False))

# Predict the point total for 2024
X_2024 = df.iloc[:, 1:15]  # columns 1-3 and 4-15 (2010-2023)
y_2024 = model.predict(X_2024)