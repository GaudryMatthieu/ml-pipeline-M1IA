from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import joblib

iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.25, random_state=42)

knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)

filename = 'model.joblib'
joblib.dump(knn, filename)