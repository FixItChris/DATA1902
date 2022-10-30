import numpy as np
import math
import pandas as pd
from sklearn.datasets import make_regression
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from sklearn.inspection import permutation_importance

rankings = pd.read_csv("Stage3/520464625/integrated_dataset.csv")
#do not drop QS2023 Academic Reputation QS2023 Citations per Faculty
rankings_restricted = rankings.dropna() 
x = rankings_restricted[["QS2023 Academic Reputation",
                        "QS2023 Citations per Faculty",
                        "QS2023 International Student Ratio",
                        "Proportion of Female Students"]
                        ]
y = rankings_restricted["THE2020 Overall Score"]
X_train, X_test, y_train, y_test = train_test_split(x, y, random_state=42)
param_grid = {'learning_rate': [0.1, 0.2, 0.3], 
              'n_estimators': [100, 500,1000],
              'min_samples_split': [2,3,4],
              'max_depth':[3,5,10,20]                
             }
reg = GradientBoostingRegressor(
    #{'alpha': 0.9, 
    # 'learning_rate': 0.1, 
    # 'max_depth': 3, 
    # 'min_samples_leaf': 2, 
    # 'min_samples_split': 2, 
    # 'n_estimators': 100}
                                loss='squared_error', 
                                learning_rate=0.1, 
                                n_estimators=100, 
                                min_samples_split=2, 
                                min_samples_leaf=2, 
                                max_depth=3, 
                                init=None, 
                                random_state=42,
                                alpha=0.9, 
                                )
reg.fit(X_train, y_train)
y_pred = reg.predict(X_test)
print(reg.predict(X_test))
print(reg.score(X_train, y_train))
print(reg.score(X_test, y_test))

mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error: {:.2f}".format(mse))
print("Root Mean Squared Error: {:.2f}".format(math.sqrt(mse)))

feature_importance = reg.feature_importances_
sorted_idx = np.argsort(feature_importance)
pos = np.arange(sorted_idx.shape[0]) + 0.5
fig = plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.barh(pos, feature_importance[sorted_idx], align="center")
plt.yticks(pos, np.array(x.columns)[sorted_idx])
plt.title("Feature Importance (MDI)")

result = permutation_importance(
    reg, X_test, y_test, n_repeats=10, random_state=42, n_jobs=2
)
sorted_idx = result.importances_mean.argsort()
plt.subplot(1, 2, 2)
plt.boxplot(
    result.importances[sorted_idx].T,
    vert=False,
    labels=np.array(x.columns)[sorted_idx],
)
plt.title("Permutation Importance (test set)")
fig.tight_layout()
plt.show()
