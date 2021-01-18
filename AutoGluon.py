import autogluon as ag
from autogluon import TabularPrediction as task

train_data = task.Dataset(X_train)

dir = ""
predictor = task.fit(train_data=train_data, label="TARGET", output_directory=dir, problem_type="regression", eval_metric="root_mean_squared_error", AG_args_fit={"use_gpu":True} )

predictor.fit_summary()

y_pred = predictor.predict(X_test)
print(f"Predictions: {y_pred}")
perf = predictor.evaluate_predictions(y_true = y_test, y_pred = y_pred, auxiliary_metrics = True)

predictor.feature_importance(X)
predictor.get_model_best()