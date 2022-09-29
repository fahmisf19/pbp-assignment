Tautan Heroku : https://pbp-assignment-fahmi.herokuapp.com/todolist

Apa kegunaan {% csrf_token %} pada elemen <form>? 

Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?

csrf token merupakan salah satu cara untuk mencegah serangan *Cross-Site Request Forgery* (CSRF). CSRF adalah serangan yang memaksa akun dari pengguna website untuk melakukan tindakan yang tidak diinginkan pada aplikasi website tersebut, di mana pengguna sebelumnya sudah mengautentikasi diri mereka sendiri. Django memiliki tag {% csrf_token %} yang diimplementasikan untuk menghindari serangan CSRF tersebut. Caranya adalah menghasilkan token di sisi server saat merender halaman website, dan memastikan aplikasi website untuk terus memeriksa ulang token ini untuk setiap permintaan yang masuk. Jika permintaan yang masuk tidak memiliki token, maka permintaan tersebut tidak akan dieksekusi.

Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.

Ya, kita bisa membuat elemen <form> secara manual, seperti yang sudah saya buat pada tugas ini. Hal tersebut bisa dilakukan dengan membuat format form secara manual pada html, dengan <label> sebagai judul dari input yang dimasukkan, dan <input> sebagai tempat pengguna meng-input pada form. Lalu, agar form tetap rapi, bisa diformat menggunakan <style>. Selain generator {{ form.as_table }} yang merender form sebagai tabel, ada juga {{ form.as_p }} yang merender form sebagai paragraph dan {{ form.as_ul }} yang merender form sebagai list.

Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

1.  User memasukkan data pada create-task.html dan menekan button submit.

2.  Ketika button submit ditekan, maka akan menjalankan action yang memanggil funtion add-task atau create_task pada views.py yang sudah di-routing sebelumnya pada urls.py.

3.  Pada function create_task, akan disimpan title pada variable x dan description pada variable y.

4.  Kemudian akan dibuat objek baru dengan user yaitu user yang merequest, date dengan mengambil datetime.now, title dengan variable x tadi, dan description dengan variable y tadi.

5.  Objek baru tersebut disimpan pada variable baru bernama new_item.

6.  Dipanggil function save() untuk menyimpan pada database.

7.  Ketika sudah selesai, halaman akan di-redirect ke todolist.html, dengan ditambah todolist baru yang sudah tersimpan pada context rendering html.

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

1.	Membuat sebuah django-app bernama todolist dengan perintah python manage.py startapp todolist

2.	Buka settings.py di folder project_django dan tambahkan aplikasi todolist ke dalam variabel INSTALLED_APPS untuk mendaftarkan django-app dibuat ke dalam proyek Django.

3.	Membuka file models.py yang ada di folder todolist dan menambahkan kode berdasarkan permintaan soal.

4.  Menjalankan perintah python manage.py makemigrations untuk mempersiapkan migrasi skema model ke dalam database Django lokal.

5.  Menjalankan perintah python manage.py migrate untuk menerapkan skema model yang telah dibuat ke dalam database Django lokal.

6.  Mendaftarkan aplikasi todolist ke dalam urls.py yang ada pada folder project_django dengan menambahkan potongan kode berikut pada variabel urlpatterns.

7.  Membuat halaman utama todolist yang memuat username pengguna, tombol Tambah Task Baru, tombol logout, serta tabel berisi tanggal pembuatan task, judul task, dan deskripsi task.

8.  Membuat function pada views.py dengan nama show_todolist untuk menampilkan halaman todolist.html

9.  Membuat function pada views.py dengan nama register yang menerima parameter request, yang berfungsi untuk menghasilkan formulir registrasi secara otomatis dan menghasilkan akun pengguna ketika data di-submit dari form.

10.  Membuat berkas HTML dengan nama register.html dan mengisinya berdasarkan apa yang ingin ditampilkan pada halaman register.

11. Menambahkan path url register ke dalam urls.py aplikasi todolist.

12. Membuat function pada views.py dengan nama login_user yang menerima parameter request, yang berfungsi untuk mengautentikasi pengguna yang ingin login.

13. Membuat berkas HTML dengan nama login.html dan mengisinya berdasarkan apa yang ingin ditampilkan pada halaman login.

14. Menambahkan path url login ke dalam urls.py aplikasi todolist.

15. Membuat function pada views.py dengan nama logout_user yang menerima parameter request, yang berfungsi untuk melakukan mekanisme logout.

16. Menambahkan button logout pada todolist.html.

17. Menambahkan path url logout ke dalam urls.py aplikasi todolist.

18. Membuat function pada views.py dengan nama show_create_task untuk menampilkan halaman form pembuatan task.

19. Membuat berkas HTML dengan nama create-task.html dan mengisinya berdasarkan apa yang ingin ditampilkan pada halaman pembuatan task, seperti input judul task dan deskripsi task.

20. Membuat function bernama create_task pada views.py untuk menangani penyimpanan data yang dinput oleh user pada form create-task.html.

21. Menambahkan path url create-task dan add-task pada urls.py aplikasi todolist.

22. Melakukan add, commit, dan push perubahan yang sudah dilakukan untuk menyimpannya ke dalam repositori GitHub pribadi. Aplikasi akan ter-deploy otomatis karena sebelumnya sudah melakukan deploy menggunakan repository tersebut.

23. Membuat dua akun pengguna dan tiga dummy data menggunakan model Task pada akun masing-masing di situs web Heroku, untuk memastikan task yang dibuat berjalan dengan semestinya pada masing-masing akun.
