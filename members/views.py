import io
import os 
import json
import joblib
import base64
import numpy as np
import pandas as pd
import urllib.parse
import plotly.express as px
import matplotlib.pyplot as plt
from django.template import loader
from django.conf import settings
from django.http import HttpResponse
from django.http import JsonResponse
from collections import Counter

from .models import Responden
from members.models import Responden
from django.db.models import Count
from logging import Logger
from django.shortcuts import render, redirect
from .forms import RespondenForm

from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import confusion_matrix, classification_report
from django.db import connection
from sklearn.metrics import accuracy_score

from django.conf import settings
from sklearn.preprocessing import StandardScaler



def members(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

"""
Data HTML
"""
# INI INDEX HTML 
def klasifikasi(request):
    total_responden = Responden.objects.count()
    
    if total_responden == 0:
        gender_counts_dict = {'Laki_laki': 0, 'Perempuan': 0}
        percentages = {'Laki_laki': 0, 'Perempuan': 0}
    else:
        gender_counts = Responden.objects.values('gender').annotate(count=Count('gender'))
        
        gender_counts_dict = {'Laki_laki': 0, 'Perempuan': 0}
        for entry in gender_counts:
            gender = entry['gender']
            if gender == 'Laki-laki':
                gender_counts_dict['Laki_laki'] = entry['count']
            elif gender == 'Perempuan':
                gender_counts_dict['Perempuan'] = entry['count']
        
        percentages = {
            'Laki_laki': (gender_counts_dict['Laki_laki'] / total_responden * 100),
            'Perempuan': (gender_counts_dict['Perempuan'] / total_responden * 100),
        }

    # Ambil data dari model Responden
    data = pd.DataFrame(list(Responden.objects.all().values(
        'pendapatan', 'produk_unik', 'harga_terjangkau', 
        'promo_diskon_pengaruh', 'banding_harga', 'rating', 
        'iklan_digital', 'campaign_influencer', 'lingkungan', 
        'desain_lebih_penting', 'kualitas_desain', 'loyal_brand', 
        'keyakinan', 'gaya_hidup', 'kelas_angka'
    )))

    # Pisahkan fitur dan target
    X = data[['pendapatan', 'produk_unik', 'harga_terjangkau', 
              'promo_diskon_pengaruh', 'banding_harga', 'rating', 
              'iklan_digital', 'campaign_influencer', 'lingkungan', 
              'desain_lebih_penting', 'kualitas_desain', 'loyal_brand', 
              'keyakinan', 'gaya_hidup']]
    y = data['kelas_angka']

    # Normalisasi data
    X = X.apply(pd.to_numeric, errors='coerce')
    X = scaler.transform(X)

    # Prediksi menggunakan model
    y_pred = model.predict(X)

    # Hitung akurasi
    accuracy = accuracy_score(y, y_pred)
    cm = confusion_matrix(y, y_pred)
    cr = classification_report(y, y_pred)

    # presentase
    accuracy_percentage = accuracy * 100
    accuracy_percentage_str = f"{accuracy_percentage:.0f}%"

    # Formatkan hasil untuk tampilan
    cm_str = str(cm)
    cr_str = str(cr)

    # hitung persentase dari setiap kelas
    unique, counts = np.unique(y_pred, return_counts=True)
    class_counts = dict(zip(unique, counts))
    total_counts = sum(class_counts.values())

    class_percentages = {
        'kompleks': (class_counts.get(1, 0) / total_counts) * 100,
        'impulsif': (class_counts.get(-1, 0) / total_counts) * 100,
        'netral': (class_counts.get(0, 0) / total_counts) * 100
    }
  
    context = {
        'total_responden': total_responden,
        'gender_counts': gender_counts_dict,
        'percentages': percentages,
        'class_counts': class_counts,
        'class_percentages': class_percentages,
        'accuracy': accuracy_percentage_str,
        'cm': cm_str,
        'cr': cr_str, 
    }
    
    return render(request, 'klasifikasi.html', context)

#grafik as frekuensi
def grafik(request):
    
    frekuensi_belanja = Responden.objects.values('frk_belanja').annotate(count=Count('id'))

    data = [{'frk_belanja': item['frk_belanja'], 'count': item['count']} for item in frekuensi_belanja]

    return JsonResponse(data, safe=False)
def grafik_html(request):
    
    return render(request, 'grafik.html')

#platform
def platform(request):
    
    platform = Responden.objects.values('platform').annotate(count=Count('id'))

    data = [{'platform': item['platform'], 'count': item['count']} for item in platform]

    return JsonResponse(data, safe=False)
def platform_html(request):
   
    return render(request, 'platform.html')

#barang
def barang(request):

    barang = Responden.objects.values('barang').annotate(count=Count('id'))

    data = [{'barang': item['barang'], 'count': item['count']} for item in barang]

    return JsonResponse(data, safe=False)
def barang_html(request):
    return render(request, 'barang.html')

#range_harga
def range_harga(request):

    range_harga = Responden.objects.values('range_harga').annotate(count=Count('id'))

    data = [{'range_harga': item['range_harga'], 'count': item['count']} for item in range_harga]

    return JsonResponse(data, safe=False)
def range_harga_html(request):
    return render(request, 'range_harga.html')

#promo_diskon
def promo_diskon(request):

    promo_diskon = Responden.objects.values('promo_diskon').annotate(count=Count('id'))

    data = [{'promo_diskon': item['promo_diskon'], 'count': item['count']} for item in promo_diskon]

    return JsonResponse(data, safe=False)
def promo_diskon_html(request):
    return render(request, 'promo_diskon.html')

#iklan
def iklan(request):
   
   iklan = Responden.objects.values('iklan').annotate(count=Count('id'))

   data = [{'iklan': item['iklan'], 'count': item['count']} for item in iklan]

   return JsonResponse(data, safe=False)
def iklan_html(request):
    return render(request, 'iklan.html')

#iklan
def desain(request):

    desain = Responden.objects.values('desain').annotate(count=Count('id'))

    data = [{'desain': item['desain'], 'count': item['count']} for item in desain]

    return JsonResponse(data, safe=False)
def desain_html(request):
    return render(request, 'desain.html')
"""
Batas Fungsi HTML
"""
# Model SVM

model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')

def add_responden(request):
    if request.method == 'POST':
        form = RespondenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('data_testing_klaf')
        else:
            form = RespondenForm()

    return render(request, 'data_testing.html', {'form':form})        

def data_testing(request):
    return render(request, 'data_testing.html')

def data_testing_klaf(request):

    # ambil dari id data yang paling baru
    latest_responden = Responden.objects.latest('id')

    # ambil data dari objek
    form_data = latest_responden.__dict__
    df_new = pd.DataFrame([form_data])

    
    X_new = df_new[['pendapatan', 'produk_unik', 'harga_terjangkau', 
                    'promo_diskon_pengaruh', 'banding_harga', 'rating', 
                    'iklan_digital', 'campaign_influencer', 'lingkungan', 
                    'desain_lebih_penting', 'kualitas_desain', 'loyal_brand', 
                    'keyakinan', 'gaya_hidup']]
    
    # normalisasi data
    X_new = X_new.apply(pd.to_numeric, errors='coerce')
    X_new = scaler.transform(X_new)

    # prediksi
    y_pred = model.predict(X_new)

    # update kolom kelas_angka di database
    latest_responden.kelas_angka = int(y_pred[0])
    latest_responden.save()

    context = {
        'predicted_class': 'Kompleks' if y_pred[0] == 1 else 'Impulsif' if y_pred[0] == -1 else 'Netral'
    }

    return render(request, 'hasil_testing.html', context)

def calculate_accuracy(request):
    # Ambil data dari model Responden
    data = pd.DataFrame(list(Responden.objects.all().values(
        'pendapatan', 'produk_unik', 'harga_terjangkau', 
        'promo_diskon_pengaruh', 'banding_harga', 'rating', 
        'iklan_digital', 'campaign_influencer', 'lingkungan', 
        'desain_lebih_penting', 'kualitas_desain', 'loyal_brand', 
        'keyakinan', 'gaya_hidup', 'kelas_angka'
    )))[31:41]

    # Pisahkan fitur dan target
    X = data[['pendapatan', 'produk_unik', 'harga_terjangkau', 
              'promo_diskon_pengaruh', 'banding_harga', 'rating', 
              'iklan_digital', 'campaign_influencer', 'lingkungan', 
              'desain_lebih_penting', 'kualitas_desain', 'loyal_brand', 
              'keyakinan', 'gaya_hidup']]
    y = data['kelas_angka']

    # Normalisasi data
    X = X.apply(pd.to_numeric, errors='coerce')
    X = scaler.transform(X)

    # Prediksi menggunakan model
    y_pred = model.predict(X)

    # Hitung akurasi
    accuracy = accuracy_score(y, y_pred)
    cm = confusion_matrix(y, y_pred)
    cr = classification_report(y, y_pred)

    # hitung persentase dari setiap kelas
    unique, counts = np.unique(y_pred, return_counts=True)
    class_counts = dict(zip(unique, counts))
    total_counts = sum(class_counts.values())

    class_percentages = {
        'kompleks': (class_counts.get(1, 0) / total_counts) * 100,
        'impulsif': (class_counts.get(-1, 0) / total_counts) * 100,
        'netral': (class_counts.get(0, 0) / total_counts) * 100
    }

    # Formatkan hasil untuk tampilan
    cm_str = str(cm)
    cr_str = str(cr)

    context = {
        'accuracy': accuracy,
        'cm': cm_str,
        'cr': cr_str,
    }
    
    result = f"Accuracy: {accuracy:.2f}\nConfusion Matrix:\n{cm_str}\nClassification Report:\n{cr_str}\nPercentages Report:\{class_percentages}"

    return HttpResponse(result)

def test(request):

    return render(request, 'test.html')

def hasil_testing(request):

    return render(request, 'hasil_testing.html')