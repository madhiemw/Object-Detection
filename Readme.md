## silahkan baca penjelasan singkat mengenai alasan pemilihan model, pemilihan dataset, evaluasi model, dan beberapa hasil analisa model terhadap beberapa kondisi pada link berikut:
https://docs.google.com/document/d/1y2x0Hc-fiZqunfPuerK7DgW0cJBy8hekGg-kLkxXnKw/edit?usp=sharing

## untuk menjalankan aplikasi endpoint yang sudah di buat lakukan langkah langkah berikut:
1. buka folder "app"
2. install beberapa library yang butuhkan, instalasi library/package dapat dilakukan di environtment manager CONDA ataupun venv, list library berada pada requirement.txt
3. setelah instalasi paackage atau library selesai download model yang sudah di train pada link berikut https://drive.google.com/file/d/1FLU_1liJzryiwW6WIauPWqingxaatdFu/view?usp=sharing
4. pindahkan model yang sudah di download ke dalam directory "app"
5. lalu run program dengan command python app.py
6. berikut adalah endpoint yang akand di hit http://localhost:5000/detect_objects (POST)
7. gunakan postman untuk melakukan testing body yang digunakan adalah form data dengan key name 'file' dan jenis data "Files" lalu input gambar dan response dari endpoint adalah gambar dan juga hasil deteksi berupa box klasifikasi jika memang model melakukan deteksi terhadap PPE yang di train.

 ## Untuk melihat history train secara lengkap dapat dilihat pada jupyter notebook yang saya lampirkan pada directory Train Notebook.
