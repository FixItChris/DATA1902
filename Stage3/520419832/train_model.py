'''
Training the Final Model
SID: 520419832

This code implements the optimal hyper-parameters specified in the choosing_model.py file, and scores
the accuracy/effectiveness of the model using a variety of measurements.

'''

## Imports
import math
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

## Reading the file & selecting columns
df = pd.read_csv("integrated_dataset.csv").dropna()
X = df[["QS2023 Academic Reputation", "QS2023 Employer Reputation", "QS2023 Faculty Student Ratio",
    "QS2023 Citations per Faculty", "QS2023 International Faculty Ratio", "QS2023 International Student Ratio"]]
y = df["THE2020 Overall Score"]


## Splitting the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state = 42)


## Creating and training the model
rf = RandomForestRegressor(n_jobs=-1, max_depth=90, max_features=3, min_samples_leaf=2,
                            min_samples_split=8, n_estimators=100, random_state=42)
rf.fit(X_train, y_train)


## Scoring the data
y_pred = rf.predict(X_test)

# Training dataset results (supplementary)
print("Training Dataset:")
mse = mean_squared_error(y_train, rf.predict(X_train))
print("Mean Squared Error: {:.5f}".format(mse))
print("Root Mean Squared Error: {:.5f}".format(math.sqrt(mse)))
print("R^2 Score: {:.5f}".format(r2_score(y_train, rf.predict(X_train))))

print()

# Testing dataset results
print("Testing Dataset:")
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error: {:.5f}".format(mse))
print("Root Mean Squared Error: {:.5f}".format(math.sqrt(mse)))
print("R^2 Score: {:.5f}".format(r2_score(y_test, y_pred)))


## Graphing feature importances
importances_rf = pd.Series(rf.feature_importances_, index=X.columns).sort_values()
ax = importances_rf.plot(kind="barh", color="lightgreen", title="Importance of QS2023 Metrics")
ax.set_xlabel("Proportional feature importance") 
plt.show()
