
from flask import Flask, render_template

app = Flask(name)

tips = [
{
"judul": "Hemat Listrik",
"isi": "Matikan lampu dan alat elektronik jika tidak digunakan."
},
{
"judul": "Gunakan Transportasi Ramah Lingkungan",
"isi": "Berjalan kaki, bersepeda, atau menggunakan transportasi umum."
},
{
"judul": "Kurangi Sampah",
"isi": "Gunakan barang yang bisa dipakai kembali dan lakukan daur ulang."
},
{
"judul": "Menanam Pohon",
"isi": "Pohon membantu menyerap karbon dioksida dari atmosfer."
},
{
"judul": "Hemat Air",
"isi": "Gunakan air secukupnya dan jangan membiarkan keran terbuka."
}
]

@app.route("/")
def home():
return render_template("index.html", tips=tips)

@app.route("/tip/int:index")
def detail(index):
if index < 0 or index >= len(tips):
return "Tips tidak ditemukan", 404

tip = tips[index]

return render_template("detail.html", tip=tip)

if name == "main":
app.run(debug=True)

detail.html

<!DOCTYPE html> <html lang="id"> <head>
<meta charset="UTF-8">

<meta name="viewport"
      content="width=device-width, initial-scale=1.0">

<title>{{ tip.judul }}</title>

<link rel="stylesheet"
      href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
<div class="container detail">


    <!-- GAMBAR SESUAI TOPIK -->

    {% if tip.judul == "Hemat Listrik" %}

        <img class="detail-image"
             src="{{ url_for('static',
             filename='images/listrik.jpg') }}"
             alt="Hemat Listrik">

    {% elif tip.judul == "Gunakan Transportasi Ramah Lingkungan" %}

        <img class="detail-image"
             src="{{ url_for('static',
             filename='images/transportasi.jpg') }}"
             alt="Transportasi Ramah Lingkungan">

    {% elif tip.judul == "Kurangi Sampah" %}

        <img class="detail-image"
             src="{{ url_for('static',
             filename='images/sampah.jpg') }}"
             alt="Kurangi Sampah">

    {% elif tip.judul == "Menanam Pohon" %}

        <img class="detail-image"
             src="{{ url_for('static',
             filename='images/pohon.jpg') }}"
             alt="Menanam Pohon">

    {% elif tip.judul == "Hemat Air" %}

        <img class="detail-image"
             src="{{ url_for('static',
             filename='images/air.jpg') }}"
             alt="Hemat Air">

    {% endif %}



    <!-- HEMAT LISTRIK -->

    {% if tip.judul == "Hemat Listrik" %}

        <h1>💡 Hemat Listrik</h1>

        <p class="subtitle">
            Cara menghemat energi listrik dalam kehidupan sehari-hari.
        </p>


        <div class="detail-box">

            <h2>1. Menghilangkan Daya Siluman</h2>

            <p>
                Perangkat elektronik yang tetap terhubung ke aliran
                listrik saat mati masih dapat mengonsumsi energi.
                Memutuskan sambungan secara total dapat mengurangi
                konsumsi daya pasif.
            </p>

        </div>


        <div class="detail-box">

            <h2>2. Efisiensi Pencahayaan</h2>

            <p>
                Menggunakan lampu hemat energi seperti LED dapat
                mengurangi penggunaan listrik karena energi yang
                digunakan lebih banyak diubah menjadi cahaya.
            </p>

        </div>


        <div class="detail-box">

            <h2>3. Mengatur Penggunaan AC</h2>

            <p>
                Mengatur suhu AC pada tingkat yang wajar dapat
                mengurangi kerja kompresor sehingga penggunaan
                energi listrik menjadi lebih rendah.
            </p>

        </div>


        <div class="detail-box">

            <h2>4. Menggunakan Perangkat Inverter</h2>

            <p>
                Perangkat dengan teknologi inverter dapat menyesuaikan
                penggunaan daya sesuai kebutuhan sehingga tidak selalu
                menggunakan daya penuh.
            </p>

        </div>



    <!-- TRANSPORTASI -->

    {% elif tip.judul == "Gunakan Transportasi Ramah Lingkungan" %}

        <h1>🚲 Gunakan Transportasi Ramah Lingkungan</h1>

        <p class="subtitle">
            Pilihan transportasi yang lebih ramah terhadap lingkungan.
        </p>


        <div class="detail-box">

            <h2>1. Berjalan Kaki dan Bersepeda</h2>

            <p>
                Berjalan kaki dan bersepeda tidak menghasilkan emisi
                langsung dari kendaraan sehingga cocok untuk perjalanan
                jarak pendek.
            </p>

        </div>


        <div class="detail-box">

            <h2>2. Menggunakan Transportasi Publik</h2>

            <p>
                Transportasi umum dapat membawa banyak penumpang
                sekaligus sehingga emisi yang dihasilkan per orang
                dapat lebih rendah dibandingkan kendaraan pribadi.
            </p>

        </div>


        <div class="detail-box">

            <h2>3. Menggunakan Kendaraan Listrik</h2>

            <p>
                Kendaraan listrik tidak menghasilkan emisi gas buang
                secara langsung ketika digunakan. Dampaknya akan semakin
                baik jika listrik berasal dari energi terbarukan.
            </p>

        </div>


        <div class="detail-box">

            <h2>4. Eco-Driving</h2>

            <p>
                Menjaga kecepatan tetap stabil dan menghindari
                percepatan mendadak dapat membantu menghemat bahan
                bakar dan mengurangi emisi kendaraan.
            </p>

        </div>
