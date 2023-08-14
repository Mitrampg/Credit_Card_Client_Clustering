# Final_Project
# Introduction
Nama = Mitra Marona Putra Gurusinga
BATCH HCK 006
Full Time Data Science
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
