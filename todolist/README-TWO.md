## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
Synchronous adalah proses jalannya program secara sequential , disini yang dimaksud sequential ada berdasarkan antrian ekseskusi program. Pada dasarnya semua Bahasa pemrograman menggunakan synchronous. Sedangkan, asynchronous adalah proses jalannya program bisa dilakukan secara bersamaan tanpa harus menunggu proses antrian. Synchronous merupakan bagian dari Asynchronous (1 antrian) dimana proses akan dieksekusi secara bersamaan dan untuk hasil tergantung lama proses suatu fungsi synchronous 

## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Event-driven adalah suatu paradigma pemrograman yang alur programnya ditentukan oleh suatu event / peristiwa yang merupakan keluaran atau tindakan pengguna, atau bisa berupa pesan dari program lainnya. Misalnya sebuah button ketika diklik akan terjadi sesuatu, maka hal tersebut merupakan sebuah event.

Pada tugas 6 ini, penerapan *event-driven programming* adalah pada *onReady* document untuk inisialisasi, *onClick* untuk button form baru, serta *onSuccess* yang dipanggil setelah pemanggilan AJAX berhasil.
 
## Jelaskan penerapan asynchronous programming pada AJAX.
Penerapan asynchronous programming pada AJAX adalah pada kode yang dituliskan secara asynchronous, akan dieksekusi di belakang thread utama atau biasa disebut main thread. Hal tersebut tidak akan membloking proses runtime atau menunggu hingga proses selesai dilakukan. Sembari menunggu proses tersebut selesai, *compiler* akan mengeksekusi perintah kode selanjutnya. Oleh karena itu, AJAX dapat digunakan untuk mengubah tampilan website berdasarkan hasil tanpa memerlukan *reload*.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Membuat views untuk menampilkan todolist menggunakan ajax, dengan membuat function `show_todolist_json`
2. Menaruh routing pada `urls.py` berdasarkan function tadi.
3. Melakukan pengambilan task menggunakan AJAX GET. Dengan melakukan GET ke endpoint JSON. Kemudian memproses setiap entry yang ada dan menambahkan html untuk tiap task menjadi card.
4. Membuat modal dengan menggunakan bootstrap, dengan menggunakan form untuk menambah task baru.
5. Tombol buat, di-*hook* dengan event `onClick` untuk melakukan AJAX POST, kemudian setelah berhasil tutup modal
6. Melakukan penampilan data menggunakan function showTas() pada AJAX untuk menampilkan list terbaru tanpa *reload* seluruh page.