import os
import joblib
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

model = joblib.load('model.joblib')
iris = load_iris()

X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.25, random_state=42
)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

report_dir = 'reports'
if not os.path.exists(report_dir):
    os.makedirs(report_dir)
    
file_path = os.path.join(report_dir, 'accuracy_report.txt')

with open(file_path, 'w') as f:
    f.write(f"accuracy : {accuracy:.2f}")

print(f"Rapport généré avec succès : {accuracy:.2f} dans {file_path}")