import mlflow
import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([[1], [2], [3]])
y = np.array([2, 4, 6])

mlflow.start_run()
model = LinearRegression().fit(X, y)
mlflow.sklearn.log_model(model, "model")
print("Model trained! Check MLflow UI.")
