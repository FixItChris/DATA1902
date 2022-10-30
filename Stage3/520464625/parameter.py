import numpy as np
import math
import pandas as pd
from sklearn import svm, datasets
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split

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
#parameters

param_grid = {'learning_rate': [0.1, 0.2, 0.3,0.4,0.5], 
              'n_estimators': [100,200,300,1000],
              'min_samples_split': [2,3,4,5,6],
              'min_samples_leaf': [1,2,3,4],
              'alpha' :[0.7,0.8,0.9],
              'max_depth':[3]                
             }

gbt = GradientBoostingRegressor()
grid_search = GridSearchCV(estimator=gbt, param_grid=param_grid, cv=3, n_jobs=-1, verbose=10)
grid_search.fit(X_train, y_train)

print(grid_search.best_params_)
