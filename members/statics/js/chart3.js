document.addEventListener('DOMContentLoaded', function () {
    fetch('/iklan/')
        .then(response => response.json())
        .then(data => {
            console.log('Data dari server:', data);
            
            const iklanLabels = data.map(item => item.iklan); 
            console.log('Iklan Labels:', iklanLabels);

            const iklanFrequency = iklanLabels.reduce((acc, label) => {
                acc[label] = (acc[label] || 0) + 1;
                return acc;
            }, {});

            const iklanData = {
                labels: Object.keys(iklanFrequency),
                datasets: [{
                    label: 'Preferensi Iklan',
                    data: Object.values(iklanFrequency),
                    backgroundColor: [
                        'rgba(75, 192, 192, 0.2)',
                        'rgba(255, 99, 132, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(255, 206, 86, 0.2)',
                        'rgba(153, 102, 255, 0.2)',
                        'rgba(255, 159, 64, 0.2)'
                    ],
                    borderColor: [
                        'rgba(75, 192, 192, 1)',
                        'rgba(255, 99, 132, 1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 206, 86, 1)',
                        'rgba(153, 102, 255, 1)',
                        'rgba(255, 159, 64, 1)'
                    ],
                    borderWidth: 1
                }]
            };

            const config = {
                type: 'doughnut',
                data: iklanData,
                options: {
                    responsive: true,
                    plugins: {
                        legend: {
                            position: 'top',
                        },
                        title: {
                            display: true,
                            text: 'Preferensi Iklan Favorit'
                        }
                    }
                }
            };

            const iklanCtx = document.getElementById('iklanChart').getContext('2d');
            new Chart(iklanCtx, config);
        })
        .catch(error => {
            console.error('Error fetching iklan data:', error);
        });
});

// Chart Json
document.addEventListener('DOMContentLoaded', function () {
    fetch('/barang/')
        .then(response => response.json())
        .then(data => {
            // Ambil data dari response
            const barangLabels = data.map(item => item.barang); 

            // Pisahkan item utama berdasarkan koma, tetapi biarkan format khusus
            const cleanedData = barangLabels.flatMap(label => {
                // Pisahkan hanya berdasarkan koma
                return label.split(/, (?=[^\s]*[A-Z])/); // Pisahkan koma sebelum huruf kapital untuk menjaga format khusus
            });

            // Hitung frekuensi setiap barang
            const barangFrequency = cleanedData.reduce((acc, barang) => {
                barang = barang.trim(); // Menghapus spasi di awal dan akhir
                if (barang.length > 0) {
                    acc[barang] = (acc[barang] || 0) + 1;
                }
                return acc;
            }, {});

            // Hitung total item
            const totalItems = cleanedData.length;

            // Hitung persentase
            const barangPercentage = Object.keys(barangFrequency).reduce((acc, barang) => {
                acc[barang] = (barangFrequency[barang] / totalItems * 100).toFixed(2);
                return acc;
            }, {});

            // Siapkan data untuk Chart.js
            const barangData = {
                labels: Object.keys(barangFrequency),
                datasets: [{
                    label: 'Barang Produk',
                    data: Object.values(barangPercentage),
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
                data: barangData,
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

            // Inisialisasi Chart.js untuk barang produk
            const barangCtx = document.getElementById('barangChart').getContext('2d');
            new Chart(barangCtx, config);
        })
        .catch(error => {
            console.error('Error fetching data:', error);
        });
});
