# Hyperparameter search with integration into LightGBM

import optuna.integration.lightgbm as lgb_o
from sklearn.model_selection import train_test_split
import sklearn.datasets
from sklearn.metrics import r2_score

#Prepare train and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

#Set data for lightGBM
train = lgb_o.Dataset(X_train, y_train)
test = lgb_o.Dataset(X_test, y_test)

#Hyperparameter search
params = {'objective': 'regression',
          'metric': 'rmse',
          'random_seed':0} 

gbm_o = lgb_o.train(params,
                    train,
                    valid_sets=test,
                    early_stopping_rounds=100,
                    verbose_eval=200,)

y_train_pred = gbm_o.predict(X_train,num_iteration=gbm_o.best_iteration)
y_test_pred = gbm_o.predict(X_test,num_iteration=gbm_o.best_iteration)

best_params = gbm_o.params
print("  Params: ")
for key, value in best_params.items():
    print("    {}: {}".format(key, value))


# Cross-validation search
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
import optuna.integration.lightgbm as lgb

X_train, y_test, y_train, y_test = train_test_split(X, y, random_state=42)

# Set data for lightgbm
train = lgb.Dataset(X_train, y_train)

tuner = lgb.LightGBMTunerCV(params, train, verbose_eval=100, early_stopping_rounds=100, folds=KFold(n_splits=3))

# Search for the hyperparameters
tuner.run()

#Show the best parameters
best_params = tuner.best_params
print(" Params: ")
for key, value in best_params.items():
    print("    {}: {}".format(key, value))