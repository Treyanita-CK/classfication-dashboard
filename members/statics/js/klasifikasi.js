const data = {
    labels: [
        'Pengaruh Pendapatan',
        'Produk atau Desain Unik',
        'Harga yang Terjangkau',
        'Promo & Diskon',
        'Rating dan Ulasan',
        'Perbandingan Harga Antar Platform',
        'Pengaruh Influencer',
        'Pengaruh Iklan',
        'Kualitas',
        'Brand',
        'Keyakinan',
        'Gaya Hidup'
    ],
    datasets: [{
        label: 'My Dataset',
        data: Array(12).fill(1), // Sama rata untuk setiap irisan
        backgroundColor: [
            '#FF6384', // Red
            '#36A2EB', // Blue
            '#FFCE56', // Yellow
            '#4BC0C0', // Teal
            '#9966FF', // Purple
            '#FF9F40', // Orange
            '#FF6394', // Light Red
            '#36C2EB', // Light Blue
            '#FFCF56', // Light Yellow
            '#4BD0C0', // Light Teal
            '#9B66FF', // Light Purple
            '#FF9F70'  // Light Orange
        ],
        hoverBackgroundColor: [
            '#FF6384',
            '#36A2EB',
            '#FFCE56',
            '#4BC0C0',
            '#9966FF',
            '#FF9F40',
            '#FF6394',
            '#36C2EB',
            '#FFCF56',
            '#4BD0C0',
            '#9B66FF',
            '#FF9F70'
        ]
    }]
};

const config = {
    type: 'pie',
    data: data,
    options: {
        responsive: true,
        plugins: {
            legend: {
                position: 'top',
            },
            title: {
                display: true,
                text: 'Pengaruh Faktor-Faktor terhadap Perilaku Konsumen'
            }
        }
    },
};

window.onload = function() {
    const ctx = document.getElementById('myPieChart').getContext('2d');
    new Chart(ctx, config);
};
