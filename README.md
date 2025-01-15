<p align="center">
  <img src="https://github.com/jith4j/Tuberculosis-Classification/blob/main/logo/logo.gif" alt="banner">
</p>

# Project Title
## Prediksi Penyakit Tuberculosis (X-ray) menggunakan metode Convolutional Neural Network

<!-- Buttons -->
![GitHub License](https://img.shields.io/github/license/jith4j/Tuberculosis-Classification)
![GitHub number of Languages](https://img.shields.io/github/languages/count/jith4j/Tuberculosis-Classification)
![GitHub top Language](https://img.shields.io/github/languages/top/jith4j/Tuberculosis-Classification?color=orange)
[![Open In Colab: ](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jith4j/Tuberculosis-Classification/blob/main/Tuber_Classification.ipynb)


Tuberkulosis (TBC) adalah salah satu penyakit menular yang menjadi penyebab utama kematian di seluruh dunia, terutama di negara berkembang. Tuberkulosis (TBC) tetap menjadi tantangan kesehatan global yang signifikan. Menurut laporan Organisasi Kesehatan Dunia (WHO) tahun 2023, terdapat sekitar 10,8 juta kasus TBC di seluruh dunia pada tahun 2023, dengan 1,25 juta kematian terkait penyakit ini.Indonesia menempati peringkat kedua dengan jumlah kasus TBC terbanyak di dunia, setelah India. menurut data kementrian kesehatan Pada tahun 2023, estimasi kasus TBC di Indonesia mencapai 1.060.000, dengan angka kematian sekitar 134.000 per tahun.Deteksi dini TBC sangat penting untuk mengurangi angka kematian dan mencegah penularan. Namun, metode deteksi tradisional, seperti tes laboratorium sputum, membutuhkan waktu dan tenaga medis yang signifikan. Oleh karena itu, pendekatan berbasis deep learning dengan menggunakan Convolutional Neural Network (CNN) menawarkan solusi inovatif untuk menganalisis citra X-ray paru-paru secara cepat dan akurat dalam mengidentifikasi pasien yang terkena TBC. Proyek ini bertujuan untuk mengembangkan model prediksi TBC berbasis CNN dengan memanfaatkan dataset X-ray paru-paru yang mengklasifikasikan gambar sebagai "normal" atau "TBC".

dalam projek ini di gunakan datset dari kagle. Dataset Tuberculosis (TB) Chest X-ray dibuat oleh tim peneliti dari Qatar University, University of Dhaka, serta kolaborator dari Malaysia dan institusi medis di Qatar dan Bangladesh. Dataset ini mencakup 700 gambar X-ray pasien TB yang dapat diakses secara publik, 2800 gambar TB tambahan yang dapat diunduh melalui portal NIAID dengan perjanjian, dan 3500 gambar normal. Data dikumpulkan dari berbagai sumber, termasuk National Library of Medicine (NLM) AS, Belarus Set, NIAID TB Portal, dan RSNA CXR dataset. Penelitian ini berhasil mengklasifikasikan TB dan gambar normal dengan akurasi 98,3%, dipublikasikan dalam IEEE Access (2020). Dataset ini dirancang untuk mendukung penelitian lebih lanjut dalam deteksi TB menggunakan deep learning.

Model analisis TBC menggunakan Convolutional Neural Network (CNN) dirancang untuk mendeteksi pola pada citra X-ray paru-paru guna membedakan kondisi normal dan TBC. Konfigurasi model CNN umumnya terdiri dari beberapa lapisan konvolusi untuk ekstraksi fitur, diikuti lapisan pooling untuk mengurangi dimensi data tanpa kehilangan informasi penting. Setelah itu, lapisan fully connected digunakan untuk melakukan klasifikasi. Model ini dapat menggunakan arsitektur populer seperti VGG16, ResNet, atau model kustom yang dioptimalkan untuk dataset X-ray. Proses pelatihan dilakukan dengan fungsi loss seperti Binary Cross-Entropy untuk masalah klasifikasi biner, serta optimisasi menggunakan algoritma seperti Adam atau SGD. Regularisasi seperti dropout sering digunakan untuk mencegah overfitting, mengingat dataset X-ray sering memiliki ukuran terbatas.

Evaluasi model dilakukan dengan menggunakan berbagai metrik performa. Akurasi digunakan untuk mengukur proporsi prediksi yang benar, tetapi karena masalah kesehatan seperti TBC memiliki implikasi serius, fokus utama adalah pada metrik seperti recall (sensitivitas), yang menunjukkan kemampuan model mendeteksi kasus positif (TBC). Precision digunakan untuk menilai seberapa akurat prediksi positif yang dihasilkan model. Selain itu, F1-Score memberikan gambaran seimbang antara presisi dan recall, terutama jika dataset tidak seimbang. ROC-AUC juga digunakan untuk mengevaluasi kemampuan model membedakan antara kelas positif dan negatif berdasarkan probabilitas prediksi. Matriks kebingungan digunakan untuk menganalisis kesalahan model secara detail, terutama untuk memahami jumlah kasus False Negative (FN), yang harus diminimalkan dalam aplikasi medis seperti ini.
Code dalam projek ini terinspirasi dari Prithviraj Pawar dengan beberapa modifikasi dan penambahan code dalam projek ini.</b>.

# Link Deploy
https://tbcbyabi.streamlit.app/


# refrensi
https://www.kaggle.com/datasets/tawsifurrahman/tuberculosis-tb-chest-xray-dataset

https://www.kaggle.com/code/prithvi10/tb-cnn-pytorch

https://www.who.int/news-room/fact-sheets/detail/tuberculosis

https://colab.research.google.com/drive/1bnFWr8qzNw_zKEqUcb8rHM08FunYhMVI?usp=sharing


