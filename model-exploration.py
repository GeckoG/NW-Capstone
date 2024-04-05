'''
This is a machine learning model that predicts the future top-100 average of track and field events.
Created on Monday, April 1st, 2024
Author: Matt Goeckel
'''
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge, Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.metrics import root_mean_squared_error, mean_absolute_error, r2_score

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

# Scale features and increase the number of iterations for Lasso
lasso_model = make_pipeline(StandardScaler(), Lasso(max_iter=10000))


models = [
    ('Linear Regression', LinearRegression()),
    ('Ridge Regression', Ridge()),
    ('Lasso Regression', lasso_model),
    ('Decision Tree Regression', DecisionTreeRegressor()),
    ('Random Forest Regression', RandomForestRegressor()),
    ('Support Vector Regression', SVR()),
    ('Gradient Boosting Regression', GradientBoostingRegressor())
]

for name, model in models:
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print(name)
    print('RMSE:', root_mean_squared_error(y_test, y_pred))
    print('MAE:', mean_absolute_error(y_test, y_pred))
    print('R^2:', r2_score(y_test, y_pred))

