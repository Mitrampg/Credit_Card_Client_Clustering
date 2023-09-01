# Final_Project
# Deployment
https://huggingface.co/spaces/mitrampg/FinalProject
# Dataset

Pada proyek ini, saya mengambil dataset dari website UCI Machine Learning Repository yang dapat diakses melalui laman berikut: https://archive.ics.uci.edu/dataset/350/default+of+credit+card+clients

Kumpulan data ini berisi informasi tentang pembayaran gagal bayar, faktor demografis, status pembayaran, riwayat pembayaran, dan laporan tagihan klien kartu kredit di Taiwan dari April 2005 hingga September 2005.

Dataset ini banyak digunakan untuk menjadi bahan pembelajaran untuk membuat model prediktif terhadap kolom default_payment yang bernilai 1 = Yes, dan 0 = No. Di mana diharapkan model prediktif tersebut dapat memprediksi apakah nasabah memiliki resiko gagal bayar di bulan berikutnya.
# Objective

Dalam proyek kali ini, saya lebih memilih untuk melakukan clustering dengan memanfaatkan informasi yang diberikan dataset ini mengenai perilaku dan status kredit setiap nasabah. Di mana pada proyek ini saya menggunakan model K-means yang sangat sesuai untuk melakukan clustering dari input berupa variabel-variabel numerik.

Melalui proyek ini, diharapkan dapat menjadi wawasan dan informasi mengenai bagaimana suatu model atau algoritma dapat melakukan pengelompokan dari setiap data angka yang diberikan sebagai input. Di mana jika dilakukan secara manual mungkin mustahil untuk melihat karakteristik data-data yang hanya berupa angka, lalu mengelompokkannya sesuai karakteristik tertentu.

Dengan menggunakan model ini, dapat dihasilkan klaster-klaster yang memiliki karakteristik tertentu berdasarkan perilaku nasabah bank dalam pembayaran kartu kredit mereka. Berdasarkan karakteristik setiap klaster ini, diharapkan dapat menjadi informasi berharga pada bank dalam menghadapi permasalahan atau melakukan marketing yang lebih efektif sesuai karakteristik setiap
# Workflow

Berikut adalah tahap pengerjaan yang saya lakukan dalam proyek ini:

1. Data loading & review

Pada tahap ini saya melakukan loading dan review singkat untuk mendapatkan informasi secara umum pada dataset saya

2. Eksplorasi analisis data (sebelum klastering)

Pada tahap ini saya melakukan eksplorasi secara keseluruhan dari dataset awal saya. Dari tahap ini saya dapat mengambil keputusan mengenai tahap selanjutnya sebelum dilakukan klastering

3. Feature Engineering

Pada tahap ini saya melakukan modifikasi beberapa kolom yang diperlukan, untuk mendapat informasi tambahan yang bisa diambil dengan mengekstrak informasi dari kolom-kolom yang sudah tersedia

4. PCA

Pada tahap ini saya melakukan Principal Components Analysis untuk mereduksi kolom-kolom dataset yang akan saya gunakan sebagai input pada modelm, untuk mendapatkan komponen-komponen yang penting dari semua kolom saya

5. K-means Model

Pada tahap ini saya melakukan klustering dengan menentukan jumlah kluster yang optimal dengan elbow dan silhouette methode

6. Eksplorasi analisis data (setelah klastering)

Pada tahap ini saya melakukan eksplorasi lebih mendalam untuk mendapatkan informasi mengenai karakteristik setiap klaster berdasarkan kolom-kolom yang penting untuk dianalisa.

# Kesimpulan

Klaster 0 (Konsumen Aktif dengan Perilaku Pembelian yang Berfluktuasi):

* ***Utilization Ratio***: Klaster ini memiliki tingkat pemanfaatan kredit yang tinggi, menunjukkan ketergantungan yang lebih besar pada fasilitas kredit yang disediakan.
  
* ***Total Payment***: Mereka memiliki pembayaran total yang lebih tinggi dengan variasi yang signifikan menunjukkan ada fluktuasi jumlah pembayaran.
  
* ***Total Bill***: Mereka cenderung memiliki tagihan yang lebih tinggi, menunjukkan konsumsi kredit yang lebih intensif.
  
* ***Trend Payment & Bill***: Ada fluktuasi signifikan antara tagihan dan pembayaran, menunjukkan potensi kesulitan keuangan atau pola pembelian yang tidak tetap.
  
* ***Duly Payer***: Klaster ini tidak memiliki nasabah yang membayar tepat waktu terus-menerus selama 6 bulan
  
* ***Delayed_Payments***: Klaster ini memiliki sejumlah besar nasabah dengan keterlambatan pembayaran, menunjukkan risiko yang lebih tinggi.
  
* ***Sequential_Delay***: Sejumlah nasabah memiliki pola keterlambatan pembayaran yang berurutan, meningkatkan risiko kredit.
  
* ***Recent Bill to Limit_amount***: Mereka mendekati atau bahkan melebihi batas kredit mereka, menunjukkan ketergantungan yang lebih besar pada kredit.

Klaster 1 (Konsumen dengan Peningkatan Konsumsi dan Potensi Kesulitan Keuangan):

* ***Utilization Ratio***: Klaster ini memanfaatkan sebagian besar dari batas kredit mereka namun tidak sepenuhnya, menunjukkan penggunaan yang lebih hati-hati.
  
* ***Total Payment***: Pembayaran total yang moderat dengan variasi pembayaran yang lebih konsisten.
  
* ***Total Bill***: Tagihan moderat namun menunjukkan potensi akumulasi hutang.
  
* ***Trend Payment & Bill***: Kenaikan yang konsisten pada tren pembayaran dan tagihan. Namun perlu diperhatikan dengan tagihan yang lebih besar dari klaster 2, mereka memiliki pembayaran yang lebih rendah dari klaster 2.
  
* ***Duly Payer***: Klaster ini tidak memiliki nasabah yang membayar tepat waktu terus-menerus selama 6 bulan
  
* ***Delayed_Payments***: Memiliki karakteristik yang sama dengan klaster 0, di mana terlalu banyak nasabah yang menunda pembayaran, dan bahkan dengan jumlah nasabah yang lebih banyak di klaster ini dibanding dengan klaster 0.
  
* ***Sequential_Delay***: Ada risiko keterlambatan berurutan yang perlu diperhatikan.
  
* ***Recent Bill to Limit_amount***: Mereka menggunakan batas kredit sama dengan klaster 0 namun dengan jumlah yang lebih sedikit.

Klaster 2 (Konsumen Stabil dan Dapat Diandalkan):

* ***Utilization Ratio***: Penggunaan kredit yang rendah menunjukkan perilaku keuangan yang konservatif.
  
* ***Total Payment***: Pembayaran yang lebih rendah namun konsisten.
  
* ***Total Bill***: Tagihan rendah menunjukkan penggunaan kredit yang lebih jarang atau hati-hati.
  
* ***Trend Payment & Bill***: Stabilitas dalam penggunaan kredit dan pembayaran menunjukkan risiko rendah.
  
* ***Duly Payer***: Memiliki 22% nasabah yang merupakan pembayar tepat waktu selama 6 bulan berturut
  
* ***Delayed_Payments***: Risiko keterlambatan mungkin rendah di klaster ini.
  
* ***Sequential_Delay***: Keterlambatan berurutan mungkin jarang terjadi, menunjukkan manajemen keuangan yang baik.
  
* ***Recent Bill to Limit_amount***: Mereka memiliki tagihan terbaru yang relatif kecil dibandingkan dengan batas kredit mereka, menunjukkan perilaku keuangan yang bijaksana.


Dari kesimpulan di atas, klaster 0 memiliki risiko kredit yang paling tinggi namun juga menawarkan peluang bisnis yang signifikan karena aktivitas kreditnya yang tinggi. Klaster 1 menunjukkan resiko yang sama dengan klaster 0, dengan nominal uang yang lebih rendah namun memiliki jumlah nasabah yang tinggi di klaster ini. Klaster 2 menunjukkan risiko kredit yang paling rendah dan mungkin merupakan target yang baik untuk penawaran kredit tambahan karena stabilitas keuangannya, namun mungkin saja klaster ini merupakan kelas ekonomi yang sederhana dengan karakter yang sangat berhati-hati dalam penggunaan kartu kredit.

# Saran Bisnis

Klaster 0 (Risiko Tinggi, Konsumen Aktif):

* Pendekatan Proaktif: Mengingat risiko yang lebih tinggi dari klaster ini, perusahaan kredit harus proaktif dalam memantau perilaku kredit nasabah dan melakukan pendekatan komunikasi yang lebih intensif untuk memahami kebutuhan dan tantangan keuangan mereka.
* Program Edukasi Keuangan: Sebagai bagian dari pendekatan proaktif, perusahaan bisa menawarkan program edukasi keuangan untuk membantu nasabah memahami manajemen hutang dan keuangan pribadi.
* Promosi Bertarget: Meskipun klaster ini menunjukkan risiko, mereka juga aktif dalam menggunakan kredit. Oleh karena itu, promosi atau penawaran yang tepat sasaran bisa efektif untuk memaksimalkan potensi pendapatan dari klaster ini tanpa meningkatkan risiko.

Klaster 1 (Risiko Sedang, Jumlah Nasabah Tinggi):

* Pembatasan Kenaikan Limit: Sebaiknya hindari meningkatkan limit kredit dengan cepat untuk klaster ini. Pendekatan yang lebih konservatif dalam menaikkan batas kredit akan lebih bijaksana.
* Program Loyalitas: Mengingat jumlah nasabah yang tinggi di klaster ini, perusahaan bisa mempertimbangkan program loyalitas untuk menghargai nasabah atas konsistensi mereka, sekaligus mendorong penggunaan kredit yang lebih bertanggung jawab.
* Pendekatan Personalisasi: Karena klaster ini memiliki jumlah nasabah yang banyak, pendekatan personalisasi melalui komunikasi atau penawaran khusus bisa efektif dalam mempertahankan dan meningkatkan hubungan dengan nasabah.

Klaster 2 (Risiko Rendah, Konsumen Hati-hati):

* Penawaran Kredit Tambahan: Mengingat risiko rendah dan stabilitas keuangan klaster ini, perusahaan bisa mempertimbangkan menawarkan produk kredit tambahan atau meningkatkan limit kredit mereka.
* Pendidikan Keuangan Lanjutan: Meskipun klaster ini menunjukkan perilaku keuangan yang baik, program edukasi keuangan lanjutan bisa membantu mereka memaksimalkan penggunaan produk kredit yang ada.
* Promosi Khusus: Mengingat sifat hati-hati mereka dalam menggunakan kredit, promosi khusus atau penawaran dengan nilai tambah bisa menjadi cara yang efektif untuk mendorong mereka untuk lebih aktif menggunakan fasilitas kredit.

# Pengembangan Penelitian

Dengan klaster yang sudah diperoleh, dapat dilakukan perbandingan dengan kolom target yang sudah ada, yaitu default_payment. Dapat dilakukan perbandingan karakteristik dari kategori default_payment dan kategori klaster. Selain itu, dengan adanya kolom klaster yang memiliki karakteristik tertentu setiap klasternya, maka kolom ini dapat digunakan sebagai target untuk pengembangan model prediktif selanjutnya.
