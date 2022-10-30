'''
Choosing the ideal hyper-parameters of the model
SID: 520419832

This code uses sklearn's GridSearchCV function to determine the ideal hyper-parameters to use for the
final random forest predictive model, found in "train_model.py".

'''

## Imports
import math
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

## Reading the dataset and selecting columns
df = pd.read_csv("integrated_dataset.csv").dropna()
X = df[["QS2023 Academic Reputation", "QS2023 Employer Reputation", "QS2023 Faculty Student Ratio",
    "QS2023 Citations per Faculty", "QS2023 International Faculty Ratio", "QS2023 International Student Ratio"]]
y = df["THE2020 Overall Score"]

## Parameter grid of hyper-parameter values to test
param_grid = {
    "max_depth": [60, 70, 80, 90, 100],
    "max_features": [2, 3, 4, 5],
    "min_samples_leaf": [2, 3, 4, 5],
    "min_samples_split": [8, 10, 12],
    "n_estimators": [100, 200, 500, 1000, 1500, 2000]
}

## Dividing the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

## Running the 5-fold GridSearchCV
rf = RandomForestRegressor(random_state=42)
grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, cv=5, n_jobs=-1, verbose=10)
grid_search.fit(X_train, y_train)

## Printing the best hyper-parameters to use in the final model
print(grid_search.best_params_)
