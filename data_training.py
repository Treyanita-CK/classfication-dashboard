import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dashboard.settings')
django.setup()

import joblib
import numpy as np
import pandas as pd
from members.models import Responden
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score

# Load Dataset dari Database
data = pd.DataFrame(list(Responden.objects.all().values()))

# Pisahkan fitur dan target
X = data[['pendapatan', 'produk_unik', 'harga_terjangkau', 
          'promo_diskon_pengaruh', 'banding_harga', 'rating', 
          'iklan_digital', 'campaign_influencer', 'lingkungan', 
          'desain_lebih_penting', 'kualitas_desain', 'loyal_brand', 
          'keyakinan', 'gaya_hidup']]
y = data['kelas_angka']

# Normalisasi
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split Data untuk Pelatihan dan Pengujian
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.4, random_state=42 )

# Latih Model SVM dengan Kernel RBF dan parameter C=10, gamma=0.01
model = SVC(C=100, gamma=0.001, kernel='rbf')
model.fit(X_train, y_train)

# Evaluasi Model
predictions = model.predict(X_test)
print("Confusion Matrix:")
print(confusion_matrix(y_test, predictions))
print("Classification Report:")
print(classification_report(y_test, predictions))
print("Accuracy Score:")
print(accuracy_score(y_test, predictions))

# Simpan Model Terlatih
#joblib.dump(model, 'model_rbf_C10_gamma0001.pkl')
#joblib.dump(scaler, 'scaler.pkl')

print("Distribusi Kelas di Data Pengujian:")
print(y_test.value_counts())

print("Distribusi Kelas di Prediksi:")
print(pd.Series(predictions).value_counts())

# Cross-validation untuk evaluasi model dengan parameter yang sudah dipilih
model_cv = SVC(C=10, gamma=0.0001, kernel='rbf')
cv_scores = cross_val_score(model_cv, X_scaled, y, cv=5, scoring='accuracy')