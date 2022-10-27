import numpy as np
import pandas as pd
from sklearn.datasets import make_regression
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split

rankings = pd.read_csv("Stage3/520464625/integrated_dataset.csv")
#do not drop QS2023 Academic Reputation QS2023 Citations per Faculty
rankings_restricted = rankings.dropna()
print(rankings_restricted)
x = rankings_restricted[["QS2023 Academic Reputation","QS2023 Citations per Faculty","QS2023 International Student Ratio","Proportion of Female Students"]]
y = rankings_restricted["THE2020 Overall Score"]
X_train, X_test, y_train, y_test = train_test_split(x, y, random_state=0)
reg = GradientBoostingRegressor(
                                loss='squared_error', 
                                learning_rate=0.1, 
                                n_estimators=1000, 
                                subsample=1.0, 
                                criterion='friedman_mse', 
                                min_samples_split=2, 
                                min_samples_leaf=1, 
                                min_weight_fraction_leaf=0.0, 
                                max_depth=3, 
                                min_impurity_decrease=0.0, 
                                init=None, 
                                random_state=0,
                                max_features=None, 
                                alpha=0.9, 
                                verbose=0, 
                                max_leaf_nodes=None, 
                                warm_start=False, 
                                validation_fraction=0.1, 
                                n_iter_no_change=None, 
                                tol=0.0001, 
                                ccp_alpha=0.0
                                )
reg.fit(X_train, y_train)
reg.predict(X_test[1:2])
print(reg.predict(X_test[1:2]))
print(reg.score(X_test, y_test))