from django.urls import path
from . import views
from .views import add_responden

urlpatterns = [
    
    path('', views.klasifikasi, name='klasifikasi'),
    path('data_testing/', views.data_testing, name='data_testing'),
    
    # add data baru
    path('add-responden/', add_responden, name='add-responden'),

    path('grafik/', views.grafik, name='grafik'),
    path('grafik-html/', views.grafik_html, name='grafik-html'),

    path('platform/', views.platform, name='platform'),
    path('platform-html/', views.platform_html, name='platform-html' ),

    path('barang/', views.barang, name='barang'),
    path('barang-html', views.barang_html, name='barang-html'),

    path('range_harga/', views.range_harga, name='range_harga'),
    path('range-harga-html/', views.range_harga_html, name='range-harga-html'),

    path('promo_diskon/', views.promo_diskon, name='promo_diskon'),
    path('promo-diskon-html/', views.promo_diskon_html, name ='promo-diskon-html'),

    path('iklan/', views.iklan, name='iklan'),
    path('iklan-html/', views.iklan_html, name='iklan-html'),

    path('desain/', views.desain, name='desain'),
    path('desain-html/', views.desain_html, name='desain-html'),

    path('data_testing/', views.data_testing, name="data_testing"),
    path('data-testing-klaf/', views.data_testing_klaf, name="data_testing_klaf"),
    path('calculate-accuracy/', views.calculate_accuracy, name="calculate_accuracy"),

    path('test/', views.test, name="test"),
    path('hasil_testing/', views.hasil_testing, name="hasil_testing")
]