import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
import statsmodels.api as sm
import numpy as np
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 100)


def get_cancer_data():
    '''load the cancer data set
    '''
    data_f_path = '.\Data\\'
    df_cancer = pd.read_csv(data_f_path + 'cancer_reg.csv')
    return df_cancer

def drop_outliers(df: pd.core.frame.DataFrame,variable:object) -> pd.core.frame.DataFrame :
    '''Takes a dataframe and variable name, calculates the interquartile range and then 50% above and below
       Then it drops the rows that are outside of those bounds and returns the datafram
    '''
    #https://medium.com/analytics-vidhya/ways-to-improve-a-linear-regression-model-e2c75fc0bdfd
    f_75_percentile = df[variable].describe()['75%']
    f_25_percentile = df[variable].describe()['25%']
    # #calculate the interquartile range
    IQR = f_75_percentile - f_25_percentile
    outlier_upper_bound = f_75_percentile + 1.5 * IQR
    outlier_lower_bound = f_25_percentile - 1.5 * IQR
    upper_outlier_indices = (df[df[variable] > outlier_upper_bound]).index
    lower_outlier_indices = (df[df[variable] < outlier_lower_bound]).index
    df.drop(index=upper_outlier_indices,inplace=True)
    df.drop(index=lower_outlier_indices,inplace=True)
    return df

def create_train_test_data_sets(df:pd.core.frame.DataFrame,response_variable:object, f_test_size:float,f_random_state: float ) -> [ pd.core.frame.DataFrame, pd.core.frame.DataFrame, pd.core.frame.DataFrame, pd.core.frame.DataFrame]:
    # divide the data up into train and test sets
    df_train, df_test = train_test_split(df, test_size = f_test_size , 
                                         random_state = f_random_state)
    # Separate the training data into two dfs, predictors (X) and response (y)
    X_train = df_train.drop(columns=[response_variable])
    y_train = df_train[response_variable]
    X_test = df_test.drop(columns=[response_variable])
    y_test = df_test[response_variable]
    return [X_train,y_train,X_test,y_test]

def standardize_training_test_data (df_x_train:pd.core.frame.DataFrame,df_y_train:pd.core.frame.DataFrame,
                                   df_x_test:pd.core.frame.DataFrame,df_y_test:pd.core.frame.DataFrame
                                   ) -> [ pd.core.frame.DataFrame, pd.core.frame.DataFrame]:
    scaler = StandardScaler()
    df_train_trans = scaler.fit_transform(df_x_train)
    df_train_trans = pd.DataFrame(df_train_trans, columns = df_x_train.columns,index=df_y_train.index)
    df_test_trans = scaler.transform(df_x_test)
    df_test_trans = pd.DataFrame(df_test_trans, columns = df_x_test.columns,index=df_y_test.index)
    return df_train_trans, df_test_trans


def statsmodel_ols (df_X,df_y) -> sm.regression.linear_model.RegressionResultsWrapper:
    mod = sm.OLS(df_y, df_X, hasconst= True)
    res = mod.fit()
    return res

def sklearn_linear_regression(df_X:pd.core.frame.DataFrame,df_y:pd.core.frame.DataFrame):
    lin_reg = LinearRegression()
    lin_reg.fit(df_X,df_y)
    y_predictions = lin_reg.predict(df_X)
    lin_mse = mean_squared_error(df_y,y_predictions)
    print('Mean Squared Error:' , lin_mse)
    lin_rmse = np.sqrt(lin_mse)
    print('Root Mean Squared Error:', lin_rmse)
    r2 = r2_score(df_y,y_predictions)
    print('R^2:',r2)
    
def sklearn_lasso_reg(df_X:pd.core.frame.DataFrame,df_y:pd.core.frame.DataFrame,tolerance:float):
    # https://towardsdatascience.com/how-to-perform-lasso-and-ridge-regression-in-python-3b3b75541ad8
    lasso = Lasso(tol=tolerance)
    parameters = {'alpha': [1e-15, 1e-10, 1e-8, 1e-4, 1e-3, 1e-2, 1, 5, 10, 20]}
    lasso_regressor = GridSearchCV(lasso, parameters, scoring='neg_mean_squared_error', cv = 5)
    lasso_regressor.fit(df_X,df_y)
    print('Mean Squared Error:',-lasso_regressor.best_score_)
    print('Root Mean Squared Error:',np.sqrt(-lasso_regressor.best_score_))

def sklearn_ridge_reg(df_X:pd.core.frame.DataFrame,df_y:pd.core.frame.DataFrame):
    # https://towardsdatascience.com/how-to-perform-lasso-and-ridge-regression-in-python-3b3b75541ad8
    ridge = Ridge()
    parameters = {'alpha': [1e-2, 1, 5, 10, 20]}  #1e-15, 1e-10, 1e-8, 1e-4, 1e-3,
    ridge_regressor = GridSearchCV(ridge, parameters, scoring='neg_mean_squared_error', cv = 5)
    ridge_regressor.fit(df_X,df_y)
    print('Mean Squared Error:',-ridge_regressor.best_score_)
    print('Root Mean Squared Error:',np.sqrt(-ridge_regressor.best_score_))
    
def sklearn_ridge_reg_predict(df_x_train:pd.core.frame.DataFrame,df_y_train:pd.core.frame.DataFrame,
                                   df_x_test:pd.core.frame.DataFrame,df_y_test:pd.core.frame.DataFrame):
    # https://towardsdatascience.com/how-to-perform-lasso-and-ridge-regression-in-python-3b3b75541ad8
    ridge = Ridge()
    parameters = {'alpha': [1e-2, 1, 5, 10, 20]}  #1e-15, 1e-10, 1e-8, 1e-4, 1e-3,
    ridge_regressor = GridSearchCV(ridge, parameters, scoring='neg_mean_squared_error', cv = 5)
    ridge_regressor.fit(df_x_train,df_y_train)
    ridge = Ridge(alpha=ridge_regressor.best_params_['alpha'])
    res = ridge.fit(df_x_train,df_y_train)
    final_predictions = ridge.predict(df_x_test)
    final_mse = mean_squared_error(df_y_test,final_predictions)
    final_rmse = np.sqrt(final_mse)
    print('final_mse:', final_mse)
    print('final_rmse:',final_rmse)
    residuals = df_y_test - final_predictions
    plt.scatter(final_predictions, residuals)
    plt.axhline(y=0, color = 'red', label = '0')
    plt.xlabel('predicted values')
    plt.ylabel('residuals')
    plt.tight_layout()
    
    print('coefficients', dict(zip(df_x_test.columns,res.coef_)))

def sklearn_linear_regression_predict(df_x_train:pd.core.frame.DataFrame,df_y_train:pd.core.frame.DataFrame,
                                   df_x_test:pd.core.frame.DataFrame,df_y_test:pd.core.frame.DataFrame) -> (
                                   pd.core.frame.DataFrame) :
    lin_reg = LinearRegression()
    lin_reg.fit(df_x_train,df_y_train)
    final_y_predictions = lin_reg.predict(df_x_test)
    final_lin_mse = mean_squared_error(df_y_test,final_y_predictions)
    print('Final Mean Squared Error:' , final_lin_mse)
    final_lin_rmse = np.sqrt(final_lin_mse)
    print('Final Root Mean Squared Error:', final_lin_rmse)
    final_r2 = r2_score(df_y_test,final_y_predictions)
    print('R^2:',final_r2,'\n')
    residuals = df_y_test - final_y_predictions
    plt.scatter(final_y_predictions, residuals)
    plt.axhline(y=0, color = 'red', label = '0')
    plt.xlabel('predicted values')
    plt.ylabel('residuals')
    plt.tight_layout()
    
    df_coeff = pd.DataFrame({'predictors':list(df_x_test.columns),'coefficients':list(lin_reg.coef_)})
    print(df_coeff)
    return df_coeff