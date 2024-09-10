// Chart Json Range Harga
document.addEventListener('DOMContentLoaded', function () {
    // Fetch data from the Django view
    fetch('/range_harga/') // Pastikan path sesuai dengan URL di urls.py
        .then(response => response.json())
        .then(data => {
            // Log data dari server untuk verifikasi
            console.log('Data dari server:', data);

            // Definisikan label yang diharapkan dari data
            const hargaLabels = data.map(item => item.range_harga); // Sesuaikan sesuai dengan struktur data JSON
            console.log('Range Harga Labels:', hargaLabels);

            // Hitung frekuensi setiap range harga
            const hargaFrequency = hargaLabels.reduce((acc, label) => {
                acc[label] = (acc[label] || 0) + 1;
                return acc;
            }, {});

            // Siapkan data untuk Chart.js
            const hargaData = {
                labels: Object.keys(hargaFrequency),
                datasets: [{
                    label: 'Range Harga',
                    data: Object.values(hargaFrequency),
                    borderColor: 'rgba(75, 192, 192, 1)',
                    backgroundColor: 'rgba(75, 192, 192, 0.2)',
                    borderWidth: 1,
                    fill: false,
                    tension: 0.1
                }]
            };

            // Konfigurasi Chart.js untuk range harga
            const config = {
                type: 'line',
                data: hargaData,
                options: {
                    responsive: true,
                    plugins: {
                        title: {
                            display: true,
                            text: 'Min and Max Settings'
                        }
                    },
                    scales: {
                        y: {
                            min: 10,
                            max: 50,
                        }
                    }
                },
            };

            // Inisialisasi Chart.js untuk range harga
            const hargaCtx = document.getElementById('hargaChart').getContext('2d');
            new Chart(hargaCtx, config);
        })
        .catch(error => console.error('Error fetching data:', error));
});

// Chart Json Promo dan Diskon
document.addEventListener('DOMContentLoaded', function () {

    fetch('/promo_diskon/') 
        .then(response => response.json())
        .then(data => {
           
            console.log('Data dari server:', data);

            const promoLabels = data.map(item => item.promo_diskon); 
            console.log('Promo Labels:', promoLabels);

            const promoFrequency = promoLabels.reduce((acc, label) => {
                acc[label] = (acc[label] || 0) + 1;
                return acc;
            }, {});

            const promoData = {
                labels: Object.keys(promoFrequency),
                datasets: [{
                    label: 'Promo',
                    data: Object.values(promoFrequency),
                    borderColor: 'rgba(75, 192, 192, 1)',
                    backgroundColor: 'rgba(75, 192, 192, 0.2)',
                    borderWidth: 1,
                    fill: false,
                    tension: 0.1
                }]
            };

            const config = {
                type: 'line',
                data: promoData,
                options: {
                    responsive: true,
                    plugins: {
                        title: {
                            display: true,
                            text: 'Promo Diskon Chart',
                        }
                    },
                    scales: {
                        y: {
                            min: 10,
                            max: 50,
                        }
                    }
                },
            };

            const promoCtx = document.getElementById('promoChart').getContext('2d');
            new Chart(promoCtx, config);
        })
        .catch(error => console.error('Error fetching data:', error));
});


// Desain 
document.addEventListener('DOMContentLoaded', function () {
    fetch('/desain/')
        .then(response => response.json())
        .then(data => {
            console.log('Data dari server:', data);
            
            // Memastikan variabel desainLabels diisi dengan benar
            const desainLabels = data.map(item => item.desain); 
            console.log('Desain Labels:', desainLabels);

            // Menghitung frekuensi setiap desain
            const desainFrequency = desainLabels.reduce((acc, label) => {
                acc[label] = (acc[label] || 0) + 1;
                return acc;
            }, {});

            // Menyiapkan data untuk Chart.js
            const desainData = {
                labels: Object.keys(desainFrequency),
                datasets: [{
                    label: 'Preferensi Desain',
                    data: Object.values(desainFrequency),
                    backgroundColor: [
                        'rgba(75, 192, 192, 0.2)',
                        'rgba(255, 99, 132, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(255, 206, 86, 0.2)'
                    ],
                    borderColor: [
                        'rgba(75, 192, 192, 1)',
                        'rgba(255, 99, 132, 1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 206, 86, 1)'
                    ],
                    borderWidth: 1
                }]
            };

            // Konfigurasi Chart.js untuk diagram donat
            const config = {
                type: 'doughnut',
                data: desainData,
                options: {
                    responsive: true,
                    plugins: {
                        legend: {
                            position: 'top',
                        },
                        title: {
                            display: true,
                            text: 'Preferensi Desain Favorit'
                        }
                    }
                }
            };

            // Mendapatkan konteks dari elemen canvas untuk Chart.js
            const desainCtx = document.getElementById('desainChart').getContext('2d');
            new Chart(desainCtx, config);
        })
        .catch(error => {
            console.error('Error fetching desain data:', error);
        });
});


// Kategori
document.addEventListener('DOMContentLoaded', function () {
    const kategoriLabels = [
        'Pakaian dan aksesoris, Produk kecantikan (skincare, makeup), Alat tulis/ alat lukis/ alat musik',
        'Pakaian dan aksesoris, Produk kecantikan (skincare, makeup)',
        'Pakaian dan aksesoris, Produk kecantikan (skincare, makeup)',
        'Pakaian dan aksesoris',
        'Pakaian dan aksesoris, Produk kecantikan (skincare, makeup)',
        'Pakaian dan aksesoris, Elektronik, Alat tulis/ alat lukis/ alat musik',
        'Pakaian dan aksesoris, Produk kecantikan (skincare, makeup)',
        'Pakaian dan aksesoris, Produk kecantikan (skincare, makeup)',
        'Elektronik',
        'Pakaian dan aksesoris, Elektronik',
        'Pakaian dan aksesoris, Peralatan rumah tangga, Produk kecantikan (skincare, makeup)',
        'Pakaian dan aksesoris, Produk kecantikan (skincare, makeup)',
        'ISO game',
        'Pakaian dan aksesoris, Elektronik, Buku',
        'Pakaian dan aksesoris, Produk kecantikan (skincare, makeup)',
        'Elektronik, Alat olahraga',
        'Pakaian dan aksesoris, Elektronik, Produk kecantikan (skincare, makeup)',
        'Pakaian dan aksesoris, Elektronik',
        'Elektronik',
        'Pakaian dan aksesoris, Produk kecantikan (skincare, makeup)',
        'Peralatan rumah tangga',
        'Pakaian dan aksesoris',
        'Pakaian dan aksesoris, Produk kecantikan (skincare, makeup), Alat olahraga',
        'Pakaian dan aksesoris, Produk kecantikan (skincare, makeup)',
        'Pakaian dan aksesoris, Elektronik, Peralatan rumah tangga, Produk kecantikan (skincare, makeup), Alat olahraga, Alat tulis/ alat lukis/ alat musik',
        'Pakaian dan akseoris'
    ];

    // Pisahkan dan bersihkan data
    const cleanedData = kategoriLabels.flatMap(label => 
        label.replace(/[\(\),]/g, '').split(/,|\/| dan /)
    );

    // Hitung frekuensi setiap kategori
    const kategoriFrequency = cleanedData.reduce((acc, kategori) => {
        kategori = kategori.trim(); // Menghapus spasi di awal dan akhir
        acc[kategori] = (acc[kategori] || 0) + 1;
        return acc;
    }, {});

    // Hitung total item
    const totalItems = cleanedData.length;

    // Hitung persentase
    const kategoriPercentage = Object.keys(kategoriFrequency).reduce((acc, kategori) => {
        acc[kategori] = (kategoriFrequency[kategori] / totalItems * 100).toFixed(2);
        return acc;
    }, {});

    // Siapkan data untuk Chart.js
    const kategoriData = {
        labels: Object.keys(kategoriFrequency),
        datasets: [{
            label: 'Kategori Produk',
            data: Object.values(kategoriPercentage),
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)',
                'rgba(199, 199, 199, 0.2)',
                'rgba(83, 102, 255, 0.2)',
                'rgba(56, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)',
                'rgba(199, 199, 199, 1)',
                'rgba(83, 102, 255, 1)',
                'rgba(56, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    };

    // Konfigurasi Chart.js untuk diagram Doughnut
    const config = {
        type: 'doughnut',
        data: kategoriData,
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'top',
                },
                title: {
                    display: true,
                    text: 'Chart.js Doughnut Chart'
                }
            }
        }
    };

    // Inisialisasi Chart.js untuk kategori produk
    const kategoriCtx = document.getElementById('kategoriChart').getContext('2d');
    new Chart(kategoriCtx, config);
});
