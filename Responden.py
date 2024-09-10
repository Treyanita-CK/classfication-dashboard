import os
import django
import pandas as pd

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dashboard.settings')

django.setup()

from members.models import Responden

data = pd.read_csv('E:\KULIAH\SKRIPSI\Data Klasifikasi\Kuisioner_2.csv', encoding='utf-8')

data.columns = data.columns.str.strip()

existing_count = 0
new_count = 0

for index, row in data.iterrows():
    Responden.objects.create(
        nama=row['nama'],
        usia=row['usia'],
        gender=row['gender'],
        etnis=row['etnis'],
        pendidikan=row['pendidikan'],
        pekerjaan=row['pekerjaan'],
        frk_belanja=row['frk_belanja'],
        platform=row['platform'],
        barang=row['barang'],
        range_harga=row['range_harga'],
        alasan=row['alasan'],
        promo_diskon=row['promo_diskon'],
        medsos=row['medsos'],
        iklan=row['iklan'],
        desain=row['desain'],
        fitur_produk=row['fitur_produk'],
        # tambahan data
        pendapatan=row['pendapatan'],
        produk_unik=row['produk_unik'],
        harga_terjangkau=row['harga_terjangkau'],
        promo_diskon_pengaruh=row['promo_diskon_pengaruh'],
        banding_harga=row['banding_harga'],
        rating=row['rating'],
        iklan_digital=row['iklan_digital'],
        campaign_influencer=row['campaign_influencer'],
        lingkungan=row['lingkungan'],
        desain_lebih_penting=row['desain_lebih_penting'],
        kualitas_desain=row['kualitas_desain'],
        loyal_brand=row['loyal_brand'],
        keyakinan=row['keyakinan'],
        gaya_hidup=row['gaya_hidup'],
        kelas=row['kelas'],
        kelas_angka=row['kelas_angka'],
    )
    new_count += 1
 
print("Data berhasil diimport ke database")