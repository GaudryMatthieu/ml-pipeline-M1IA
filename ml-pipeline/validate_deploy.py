import os, shutil, sys

report_path = 'reports/accuracy_report.txt'
with open(report_path, 'r') as f:
    accuracy = float(f.read().split(': ')[1])

if accuracy > 0.9:
    if not os.path.exists('production'): os.makedirs('production')
    shutil.copy('model.joblib', 'production/model_prod.joblib')
    print("SUCCESS: Modèle déployé en production.")
else:
    print(f"FAILED: Accuracy {accuracy} trop basse.")
    sys.exit(1)