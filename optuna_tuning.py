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


# Hyperparameter Tuning for CatBoost
import catboost as cb
import numpy as np

import optuna

def objective(trial):
    params = {
        "iterations": trial.suggest_int("iterations", 50, 300),
        "depth": trial.suggest_int("depth", 4, 10),
        "learning_rate": trial.suggest_loguniform("learning_rate", 0.001, 0.5),
        "random_strength": trial.suggest_int("random_strength", 0, 100),
        "bagging_temperature": trial.suggest_loguniform(
            "bagging_temperature", 0.01, 100.00
        ),
        "od_type": trial.suggest_categorical("od_type", ["IncToDec", "Iter"]),
        "od_wait": trial.suggest_int("od_wait", 10, 50),
        "verbose": True,
        "task_type": "GPU"
    }
    categorical_cat = np.where(train_df.dtypes != np.float)[0]

    gbm = cb.CatBoostRegressor(**params)
    gbm = gbm.fit(X_train, y_train, cat_features=categorical_cat, eval_set=[(X_test, y_test)], verbose=0, early_stopping_rounds=100,plot=True)

    y_pred = gbm.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    print(f"RMSE: {rmse}")
    return rmse


study_cat = optuna.create_study(direction="minimize")
study_cat.optimize(objective, n_trials=100, timeout=300)

print("Number of finished trials: {}".format(len(study_cat.trials)))
print("Best trial:")
trial = study_cat.best_trial
print("  Value: {}".format(trial.value))
print("  Params: ")
for key, value in trial.params.items():
    print("    {}: {}".format(key, value))