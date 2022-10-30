import pandas as pd
from math import sqrt
from sklearn import linear_model
from sklearn import metrics
from sklearn.model_selection import train_test_split
df = pd.read_csv('../integrated_dataset.csv').dropna()

# Making our predictive model (named as 'regression_model' <- this is the model)
x = df[['QS2023 Academic Reputation','QS2023 Citations per Faculty']] 
y = df['THE2020 Overall Score']
x_trainingset, x_testset, y_trainingset, y_testset = train_test_split(x, y, test_size=0.1, random_state=42)
regression_model = linear_model.LinearRegression().fit(x_trainingset, y_trainingset)

#y_pred is the actual model in work in terms of predicting our dependent variable

y_pred = regression_model.predict(x_testset)

#Measures of success
# 1. Root mean squared error
mse = metrics.mean_squared_error(y_testset, y_pred)
print('Root mean squared error (RMSE):', sqrt(mse))

# 2. R-squared score: 1 is perfect prediction
print('R-squared score:', metrics.r2_score(y_testset, y_pred))

#Coefficients of the linear model: Which one is a better correlator? 
print(regression_model.coef_)
