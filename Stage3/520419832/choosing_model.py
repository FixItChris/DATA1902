import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Selecting columns
df = pd.read_csv("integrated_dataset.csv").dropna()
X = df[["QS2023 Academic Reputation", "QS2023 Employer Reputation", "QS2023 Faculty Student Ratio", "QS2023 Citations per Faculty", "QS2023 International Faculty Ratio"]]
y = df["THE2020 Overall Score"]

# Parameter grid - update values
param_grid = {
    "bootstrap": [True],
    "max_depth": [80, 90, 100, 110],
    "max_features": [2, 3],
    "min_samples_leaf": [3, 4, 5],
    "min_samples_split": [8, 10, 12],
    "n_estimators": [100, 200, 300, 1000]
}


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state = 42)

rf = RandomForestRegressor()
#rf.fit(X_train, y_train)
#y_pred = rf.predict(X_test)

grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, cv=3, n_jobs=-1, verbose=2)
grid_search.fit(X_train, y_train)

print(grid_search.best_params_)


#mse = mean_squared_error(y_test, y_pred)
#print("Mean Squared Error: {:.2f}".format(mse))
#print("Root Mean Squared Error: {:.2f}".format(math.sqrt(mse)))

#print(pd.DataFrame({"predicted":y_pred, "actual":y_test}))

#importances_rf = pd.Series(rf.feature_importances_, index=X.columns).sort_values()
#importances_rf.plot(kind="barh", color="lightgreen")
#plt.show()
