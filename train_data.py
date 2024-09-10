import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dashboard.settings')
django.setup()

import joblib
import numpy as np
import pandas as pd

from members.models import Responden

# algoritma support svector machine dan evaluasi confusion matriks
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, GridSearchCV

# visual
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D

# 1. Ambil data
df = Responden.objects.all().values(
    'pendapatan', 'produk_unik', 'harga_terjangkau', 'promo_diskon_pengaruh',
    'banding_harga', 'rating', 'iklan_digital', 'campaign_influencer',
    'lingkungan', 'desain_lebih_penting', 'kualitas_desain', 'loyal_brand',
    'keyakinan', 'gaya_hidup', 'kelas_angka'
)[:40]
data = pd.DataFrame.from_records(df)

# 2. Inisial Kelas
X = data.drop(['kelas_angka'], axis=1)
y = data['kelas_angka']

# 3. Normalisasi data menggunakan scaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 4. Split Data untuk Pelatihan dan Pengujian
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.4, random_state=42)

# 5. Find optimal parameters
param_grid = {
    'C': [0.1, 1, 10, 100],
    'gamma': [1, 0.1, 0.01, 0.001],
    'kernel': ['rbf']
}

grid = GridSearchCV(SVC(), param_grid, refit=True, verbose=2, cv=5)
grid.fit(X_train, y_train)

print("Best Parameters:", grid.best_params_)

# 6. Latih Model SVM dengan Kernel RBF
#model = SVC(C=10, gamma=0.01, kernel='rbf')
model = SVC(C=grid.best_params_['C'], gamma=grid.best_params_['gamma'], kernel='rbf')
model.fit(X_train, y_train)

# 7. Evaluasi Model
predictions = model.predict(X_test)
print("Confusion Matrix:")
print(confusion_matrix(y_test, predictions))
print("Classification Report:")
print(classification_report(y_test, predictions))
print("Accuracy Score:")
print(accuracy_score(y_test, predictions))


# 9. Simpan Model Terlatih
"""
joblib.dump(model, 'model.pkl')
joblib.dump(scaler, 'scaler.pkl')
"""

"""selected_features = ['kompleks', 'normal', 'impulsif']
X_visualize = data[selected_features]
X_visualize_scaled = scaler.fit_transform(X_visualize)

# 11. Visual 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X_visualize_scaled[:, 0], X_visualize_scaled[:, 1], X_visualize_scaled[:, 2], c=y, cmap='viridis', marker='o')

# Label
ax.set_xlabel(selected_features[0])
ax.set_ylabel(selected_features[1])
ax.set_zlabel(selected_features[2])

# Hyperplane
ax.view_init(elev=20., azim=30)
plt.show()"""