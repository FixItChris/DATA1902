import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Selecting columns
df = pd.read_csv("integrated_dataset.csv").dropna()
X = df[["QS2023 Academic Reputation", "QS2023 Employer Reputation", "QS2023 Faculty Student Ratio",
    "QS2023 Citations per Faculty", "QS2023 International Faculty Ratio"]]
y = df["THE2020 Overall Score"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state = 42)

rf = RandomForestRegressor(n_jobs=-1, max_depth=60, max_features=3, min_samples_leaf=2,
                            min_samples_split=8, n_estimators=100)
rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)

print("training data")
mse = mean_squared_error(y_train, rf.predict(X_train))
print("Mean Squared Error: {:.2f}".format(mse))
print("Root Mean Squared Error: {:.2f}".format(math.sqrt(mse)))

print("testing data")
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error: {:.2f}".format(mse))
print("Root Mean Squared Error: {:.2f}".format(math.sqrt(mse)))

importances_rf = pd.Series(rf.feature_importances_, index=X.columns).sort_values()
importances_rf.plot(kind="barh", color="lightgreen")
plt.show()
