# app.py
import streamlit as st

def main():

    st.set_page_config(page_title="Credit Card Clients Clustering", page_icon="hacktiv8.jpeg")
    
    col1, col2, col3 = st.columns([1, 5, 2])
    
    col1.image("hacktiv8.jpeg", width=100)
    
    col2.title("Credit Card Clients Clustering")
    
    col3.write("by: Mitra Gurusinga")

    st.title("Exploratory Data Analysis")

    # Cek apakah state sudah ada
    if 'show_explanation' not in st.session_state:
        st.session_state.show_explanation = [False, False, False, False, False, False, False, False]
    if 'selected_images' not in st.session_state:
        st.session_state.selected_images = ["Utilization Ratio", "Total Payment", "Total Bill", "Trend Payment & Bill", "Duly Payer", "Delayed Payments", "Sequential Delay", "Recent Bill to Limit"]

    # Pilihan gambar dengan default semua gambar terpilih
    pilihan_gambar = st.multiselect("Pilih Fitur Data:", ["Utilization Ratio", "Total Payment", "Total Bill", "Trend Payment & Bill", "Duly Payer", "Delayed Payments", "Sequential Delay", "Recent Bill to Limit"], default=st.session_state.selected_images)

    # Tampilkan gambar berdasarkan pilihan
    if "Utilization Ratio" in pilihan_gambar:
        st.header("Utilization Ratio")
        st.write("""
        Fitur ini menunjukkan seberapa besar dari batas kredit yang digunakan oleh pelanggan setiap bulannya. Rasio pemanfaatan memberikan gambaran tentang seberapa besar seorang pelanggan menggunakan kredit mereka dibandingkan dengan batas maksimum yang mereka miliki. Sebuah rasio yang tinggi bisa mengindikasikan bahwa pelanggan tersebut bergantung pada kredit mereka, sementara rasio yang rendah bisa menunjukkan bahwa mereka menggunakan kredit mereka dengan bijak dan dalam batas kemampuan mereka.
        """)     
        st.image("UR1.png")
        if st.button('Explain Utilization Ratio'):
            st.session_state.show_explanation[0] = not st.session_state.show_explanation[0]
        if st.session_state.show_explanation[0]:
            st.write("""
            - Klaster 0 dan Klaster 1 terdiri dari pelanggan yang cenderung memanfaatkan sebagian besar dari batas kredit mereka. Ini dapat mengindikasikan bahwa kelompok pelanggan ini mungkin lebih bergantung pada kredit mereka. 
            - Klaster 2 terdiri dari pelanggan yang sangat hati-hati dalam menggunakan kredit mereka, dengan sebagian besar memiliki "Utilization Ratio" yang rendah.
            
            Berdasarkan hal ini, dapat dipertimbangkan strategi pemberian kredit yang berbeda untuk setiap klaster, atau bahkan program edukasi keuangan untuk klaster tertentu yang tampaknya bergantung pada kredit mereka.
            """)

    if "Total Payment" in pilihan_gambar:
        st.header("Total Payment")
        st.write("""
        Total pembayaran menggambarkan jumlah total yang telah dibayarkan oleh pelanggan selama periode enam bulan. Jumlah yang lebih besar menunjukkan bahwa pelanggan tersebut telah melakukan banyak pembayaran, yang mungkin mengindikasikan kepatuhan yang baik terhadap kewajiban keuangan mereka. Sebaliknya, total pembayaran yang lebih rendah mungkin menandakan bahwa pelanggan tersebut jarang membayar atau membayar dalam jumlah yang kecil, yang mungkin mengindikasikan potensi risiko gagal bayar di masa depan.
        """)     
        st.image("TP1.png")
        if st.button('Explain Total Payment'):
            st.session_state.show_explanation[1] = not st.session_state.show_explanation[1]
        if st.session_state.show_explanation[1]:
            st.write("""
            - Klaster 0 berisi pelanggan dengan pembayaran total yang lebih tinggi dan variasi yang lebih besar dalam pembayaran mereka.
            - Klaster 1 berisi pelanggan dengan pembayaran total yang moderat dan variasi pembayaran yang lebih konsisten.
            - Klaster 2 berisi pelanggan dengan pembayaran total yang lebih rendah dan variasi pembayaran yang paling konsisten. Informasi ini dapat membantu institusi kredit memahami bagaimana perilaku pembayaran pelanggan bervariasi antar klaster dan dapat digunakan untuk merancang strategi atau intervensi yang sesuai.
            """)

    if "Total Bill" in pilihan_gambar:
        st.header("Total Bill")
        st.write("""
        Total tagihan menggambarkan jumlah total tagihan yang diterima oleh pelanggan selama periode enam bulan. Jumlah yang lebih besar menunjukkan bahwa pelanggan tersebut memiliki beban hutang yang lebih tinggi selama periode tersebut, sementara jumlah yang lebih rendah mengindikasikan hutang yang lebih rendah.
        """)     
        st.image("TB1.png")
        if st.button('Explain Total Bill'):
            st.session_state.show_explanation[2] = not st.session_state.show_explanation[2]
        if st.session_state.show_explanation[2]:
            st.write("""
            - Klaster 0: Pelanggan dengan tagihan lebih tinggi, mungkin merupakan pelanggan premium atau mereka yang menggunakan kredit dengan intensitas tinggi.
            - Klaster 1: Pelanggan dengan tagihan moderat, mungkin merupakan pelanggan dengan kebutuhan kredit yang sedang.
            - Klaster 2: Pelanggan dengan tagihan rendah, mungkin merupakan pelanggan yang jarang menggunakan kredit atau baru mulai menggunakan fasilitas kredit.
            """)
            
    if "Trend Payment & Bill" in pilihan_gambar:
        st.header("Trend Payment & Bill")
        st.write("""
        Berdasarkan dataset yang saya miliki, terdapat kolom-kolom payment dan bill yang dicatat dari histori per bulan setiap nasabah. Dengan demikian saya melakukan analisa terkait trend perubahan pembayaran dan tagihan setiap kluster. Hal ini dapat memiliki manfaat-manfaat sebagai berikut:
        
        Tren Pembayaran (trend_payment):
        
        - Mengungkapkan bagaimana perilaku pembayaran pelanggan berubah, memungkinkan identifikasi risiko yang lebih baik.
        - Membantu dalam personalisasi layanan, memastikan komunikasi yang tepat dengan pelanggan.
        - Menyoroti perubahan dalam kepatuhan pelanggan, mendorong perusahaan untuk menyesuaikan produk dan strategi mereka.
        
        Tren Tagihan (trend_bill):
        
        - Menunjukkan fluktuasi dalam beban hutang pelanggan, memberikan gambaran tentang perilaku penggunaan kredit.
        - Berfungsi sebagai alat prediksi untuk meramalkan penerimaan masa depan.
        - Mengidentifikasi potensi risiko atau peluang berdasarkan perbandingan antara penggunaan kredit dengan pembayaran yang dilakukan.
        """)     
        st.image("TPB1.png")
        st.image("TPB2.png")
        if st.button('Explain Trend Payment & Bill'):
            st.session_state.show_explanation[2] = not st.session_state.show_explanation[2]
        if st.session_state.show_explanation[2]:
            st.write("""
            Klaster 0:
            
            - Pembayaran: Klaster 0 menunjukkan tren pembayaran yang relatif stabil dengan sedikit peningkatan dari bulan ke bulan.
            - Tagihan: Untuk klaster ini, jumlah tagihan menurun dari April hingga Juni, kemudian stabil dari Juni hingga September. Jika kita membandingkan tren pembayaran dan tagihan, tampak bahwa pembayaran relatif konsisten meskipun tagihan menurun, yang mengindikasikan bahwa kelompok ini berupaya memenuhi kewajiban pembayarannya meskipun beban hutang mereka menurun.
            
            Klaster 1:
            
            - Pembayaran: Ada peningkatan signifikan dalam pembayaran dari April hingga Juni, kemudian tetap stabil hingga September.
            - Tagihan: Tagihan juga menunjukkan peningkatan dari April hingga Juni, kemudian sedikit menurun hingga September. Tren pembayaran dan tagihan mirip, dengan pembayaran yang meningkat seiring dengan peningkatan tagihan. Hal ini menunjukkan bahwa kelompok ini cenderung membayar lebih banyak saat tagihan mereka meningkat.
            
            Klaster 2:
            
            - Pembayaran: Klaster 2 memiliki pembayaran yang paling konsisten dan tinggi di antara semua klaster, dengan sedikit peningkatan dan penurunan dari bulan ke bulan. Hal ini dapat disebut juga dengan trend sideways pembayaran
            - Tagihan: Jumlah tagihan untuk klaster ini juga meningkat secara konsisten dari bulan ke bulan, namun tidak terlalu signifikan, yang juga dapat disebut trend sideways.            """)
    
    if "Duly Payer" in pilihan_gambar:
        st.header("Duly Payer")
        st.write("""
        Fitur ini menandakan apakah pelanggan selalu membayar tepat waktu selama 6 bulan terakhir. Kolom ini akan memiliki nilai 1 untuk pelanggan yang selalu membayar tepat waktu (dari bulan September hingga April) dan 0 untuk pelanggan yang memiliki setidaknya satu bulan di mana mereka tidak membayar tepat waktu.
        """)     
        st.image("DP1.png")
        if st.button('Explain Duly Payer'):
            st.session_state.show_explanation[2] = not st.session_state.show_explanation[2]
        if st.session_state.show_explanation[2]:
            st.write("""
            Berdasarkan plot pie chart di atas, dapat terlihat dengan jelas bahwa untuk nasabah yang konsisten membayar tepat waktu hanya ada pada klaster 2 dengan persentase 23,2% dari klaster 2 sebanyak 1992 nasabah. 
            """)
    
    if "Delayed Payments" in pilihan_gambar:
        st.header("Delayed Payments")
        st.write("""
        Fitur ini menghitung berapa kali seorang pelanggan terlambat membayar selama enam bulan. Jika seorang pelanggan memiliki banyak keterlambatan pembayaran, ini menunjukkan pola perilaku yang mungkin berisiko bagi pemberi kredit. Pelanggan dengan angka yang lebih tinggi untuk fitur ini mungkin dianggap lebih berisiko dari segi kemungkinan gagal bayar di masa depan.
        """)     
        st.image("DEP1.png")
        if st.button('Explain Delayed Payments'):
            st.session_state.show_explanation[2] = not st.session_state.show_explanation[2]
        if st.session_state.show_explanation[2]:
            st.write("""
            - Klaster 0: Nasabah di klaster ini cenderung memiliki perilaku pembayaran yang tertunda yang sangat konsisten, dengan memiliki persentase sebesar 90% dari total klaster yang memiliki nilai delayed_payments sebesar 6. Ini menunjukkan bahwa pelanggan di klaster ini memiliki pola tertunda dalam pembayaran mereka sepanjang waktu.
            
            - Klaster 1: Nasabah di klaster ini, memiliki karakteristik delayed_payments yang sama dengan klaster 0, dengan jumlah kelompok nasabah yang lebih banyak. Hal ini menunjukkan resiko yang lebih tinggi untuk klaster ini bagi bisnis.
            
            - Klaster 2: Klaster ini menunjukkan variasi yang paling besar dalam perilaku pembayaran. Ada pelanggan yang selalu membayar tepat waktu (nilai 0), tetapi ada juga pelanggan yang memiliki beberapa bulan tertunda dalam pembayaran mereka. Visualisasi di atas ini menunjukkan bahwa ada sejumlah pelanggan di klaster ini yang memiliki perilaku pembayaran yang baik, sementara yang lainnya memiliki perilaku pembayaran yang tertunda.
            
            Dapat dilihat bahwa delayed_payments adalah indikator penting dari perilaku pembayaran pelanggan. Klaster dengan nilai tertunda yang tinggi menunjukkan risiko yang lebih besar, karena pelanggan ini lebih cenderung memiliki pola pembayaran yang tidak konsisten atau tertunda. Sebaliknya, klaster dengan variasi yang lebih besar dalam perilaku pembayaran menunjukkan adanya peluang untuk mengidentifikasi dan mendukung pelanggan yang memiliki perilaku pembayaran yang lebih baik.
            """)
            
    if "Sequential Delay" in pilihan_gambar:
        st.header("Sequential Delay")
        st.write("""
        Fitur ini menentukan apakah pelanggan mengalami keterlambatan pembayaran berturut-turut selama tiga bulan terakhir. Keterlambatan berturut-turut menunjukkan pola perilaku pembayaran yang memburuk dan mungkin lebih berisiko bagi pemberi kredit.
        """)     
        st.image("SD1.png")
        if st.button('Explain Sequential Delay'):
            st.session_state.show_explanation[2] = not st.session_state.show_explanation[2]
        if st.session_state.show_explanation[2]:
            st.write("""
            - Klaster 0: Mayoritas pelanggan di klaster ini tidak memiliki riwayat keterlambatan pembayaran berturut-turut di 3 bulan terakhir. Hanya sebagian kecil dari pelanggan di klaster ini yang memiliki riwayat keterlambatan pembayaran berturut-turut.
            - Klaster 1: Sama seperti klaster 0, mayoritas pelanggan di klaster ini tidak memiliki riwayat keterlambatan pembayaran 3 bulan berturut-turut, dengan hanya sebagian yang ada keterlambatan pembayaran berturut-turut. Namun perbedaannya klaster ini memiliki persentase perbandingan yang lebih besar pada nasabah yang memiliki keterlambatan. Klaster 2: Mayoritas dari klaster ini tidak memiliki keterlambatan pembayaran 3 bulan terakhir. Walaupun juga ada beberapa nasabah yang memiliki pembayaran terlambat secara berturut-turut 3 bulan terakhir, namun jumlah ini sangat sedikit.
            
            Secara umum setiap klaster masih memiliki karakter yang sama, yaitu memiliki nasabah yang tidak melakukan keterlambatan pembayaran secara berturut-turut dalam 3 bulan terakhir dan ada yang melakukan keterlambatan. Namun jika dibandingkan dengan persentase perbandingan jumlah yang memiliki keterlambatan berturut dengan yang tidak, maka resiko tertinggi ada di klaster 1 dengan 9,2% persentase nasabah yang memiliki keterlambatan.
            """)
            
    if "Recent Bill to Limit" in pilihan_gambar:
        st.header("Recent Bill to Limit")
        st.write("""
        Fitur ini menunjukkan rasio tagihan bulan September (bulan terakhir di dataset) dibandingkan dengan limit kredit pelanggan. Rasio yang mendekati 1 mengindikasikan bahwa pelanggan hampir mencapai batas kredit mereka, sementara rasio yang rendah mengindikasikan penggunaan kredit yang lebih bijak dan hati-hati.
        """)     
        st.image("RB1.png")
        if st.button('Explain Recent Bill to Limit'):
            st.session_state.show_explanation[2] = not st.session_state.show_explanation[2]
        if st.session_state.show_explanation[2]:
            st.write("""
            - Klaster 0: Klaster ini memiliki rata-rata nilai "Recent Bill to Credit" yang paling tinggi. Ini menandakan bahwa nasabah dalam klaster ini cenderung hampir melebihi batas kredit mereka dalam tagihan terbaru mereka. Ini bisa menjadi tanda bahwa mereka bergantung pada kredit mereka atau mungkin mereka membelanjakan lebih banyak daripada yang mereka mampu.
            
            - Klaster 1: Nasabah dalam klaster ini memiliki rata-rata nilai "Recent Bill to Credit" yang berada di antara Klaster 0 dan Klaster 2. Meskipun tidak setinggi Klaster 1, nasabah di sini tampaknya menggunakan sebagian besar dari kredit yang tersedia untuk mereka.
            
            - Klaster 2: Klaster ini memiliki rata-rata nilai "Recent Bill to Credit" yang paling rendah dibandingkan dengan dua klaster lainnya. Ini menunjukkan bahwa nasabah dalam klaster ini cenderung memiliki tagihan terbaru yang relatif kecil dibandingkan dengan batas kredit mereka. Dengan kata lain, nasabah di klaster ini tampaknya menggunakan kredit mereka dengan lebih bijak dan berada dalam batas yang aman dari batas kredit yang diberikan.
            
            Dalam konteks bisnis, memahami perilaku penggunaan kredit ini penting. Untuk Klaster 0, misalnya, mungkin diperlukan pendekatan yang lebih hati-hati dalam memberikan penawaran kredit tambahan atau meningkatkan batas kredit mereka, mengingat perilaku penggunaan kredit mereka yang tinggi. Sedangkan untuk Klaster 2, mungkin ada peluang untuk menawarkan peningkatan batas kredit atau produk kredit lainnya, mengingat perilaku penggunaan kredit mereka yang lebih konservatif.
            """)
            
    # Reset keadaan show_explanation ketika pilihan gambar berubah
    last_option = st.session_state.get("last_option", [])
    if set(last_option) != set(pilihan_gambar):
        st.session_state.show_explanation = [False, False, False, False, False, False, False, False]
    st.session_state.last_option = pilihan_gambar

if __name__ == "__main__":
    main()
