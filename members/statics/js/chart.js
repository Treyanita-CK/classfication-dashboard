// FREKUENSI BELANJA
google.charts.load('current', {'packages':['bar']});
google.charts.setOnLoadCallback(drawChart);

function drawChart() {
    fetch('/grafik/')
        .then(response => response.json())
        .then(data => {
            // Membuat DataTable Google Charts
            const dataTable = new google.visualization.DataTable();
            dataTable.addColumn('string', 'Frekuensi Belanja');
            dataTable.addColumn('number', 'Jumlah');
            
            // Menambahkan data ke DataTable
            data.forEach(item => {
                dataTable.addRow([item.frk_belanja, item.count]);
            });

            // Opsi untuk grafik batang horizontal
            const options = {
                chart: {
                    title: 'Frekuensi Belanja',
                },
                bars: 'horizontal', // Menampilkan batang horizontal
                hAxis: {
                    title: 'Jumlah',
                },
                vAxis: {
                    title: 'Frekuensi Belanja',
                },
                colors: ['#1b9e77']
            };

            // Menggambar grafik
            const chart = new google.charts.Bar(document.getElementById('bar-chart'));
            chart.draw(dataTable, google.charts.Bar.convertOptions(options));
        })
        .catch(error => console.error('Error fetching data:', error));
}