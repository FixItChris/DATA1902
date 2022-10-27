import pandas as pd
from sklearn.datasets import make_regression
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split

rankings = pd.read_csv("Stage3/520464625/integrated_dataset.csv")
#do not drop QS2023 Academic Reputation QS2023 Citations per Faculty
rankings_restricted = rankings.dropna()
x = rankings_restricted[["QS2023 Academic Reputation","QS2023 Citations per Faculty","QS2023 International Student Ratio","Proportion of Female Students"]]
y = rankings_restricted["THE2020 Overall Score"]
X_train, X_test, y_train, y_test = train_test_split(x, y, random_state=0)
reg = GradientBoostingRegressor(random_state=0)
reg.fit(X_train, y_train)
reg.predict(X_test[1:2])
reg.score(X_test, y_test)