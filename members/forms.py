from django import forms
from members.models import Responden

class RespondenForm(forms.ModelForm):
    class Meta:
        model = Responden
        fields = ['nama', 'gender', 'frk_belanja','platform','barang','range_harga',
                  'alasan', 'promo_diskon', 'medsos', 'iklan', 'desain', 'fitur_produk',
                  'pendapatan', 'produk_unik', 'harga_terjangkau', 'promo_diskon_pengaruh', 
                  'banding_harga', 'rating', 'iklan_digital', 'campaign_influencer', 
                  'lingkungan', 'desain_lebih_penting', 'kualitas_desain', 'loyal_brand',
                  'keyakinan','gaya_hidup']