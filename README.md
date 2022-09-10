Link Heroku App : https://pbp-assignment-fahmi.herokuapp.com/katalog

**Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;**

Bagan: 

![Bagan](https://drive.google.com/uc?export=view&id=1cMwqWUmwju5w1-vjYqd3etOm-BDXcot0)

urls.py berperan sebagai routing terhadap permintaan yang masuk

views.py berperan sebagai logika utama dari aplikasi yang akan melakukan pemrosesan terhadap permintaan yang masuk

models.py berperan sebagai objek yang mendefinisikan entitas pada database beserta konfigurasinya

berkas html di sini sebagai apa yang ditampilkan kepada user

Alur permintaannya yaitu pertama permintaan yang masuk akan diproses melalui urls untuk diteruskan ke views yang didefinisikan untuk memproses permintaan tersebut. Apabila terdapat proses yang membutuhkan database, maka views akan memanggil query ke models dan database akan mengembalikan hasil query tersebut ke views. Setelah permintaan berhasil diproses, hasil proses tersebut akan dipetakan ke dalam html yang sudah didefinisikan sebelumnya, dan halaman html akan tersebut dikembalikan ke user sebagai respons.

**Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?**

Karena virtual environment di sini berfungsi untuk memisahkan pengaturan, package, serta dependencies yang diinstal pada setiap proyek Django, sehingga perubahan yang dilakukan pada satu proyek tidak mempengaruhi proyek lainnya. Jika tanpa menggunakan virtual environment, kita masih dapat membuat aplikasi web berbasis django, dengan menginstal libraries secara global. Akan tetapi, memang lebih baik kita menggunakan virtual environment saat membuat aplikasi berbasis django.

**Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.**

1. git clone repositori pada komputer, kemudian membuat virtual environment, dan menyalakan virtual environment tersebut, lalu menginstal semua dependencies yang ada pada requirements.txt
2. Menjalankan perintah python manage.py makemigrations untuk mempersiapkan migrasi skema model ke dalam database Django lokal.
3. Menjalankan perintah python manage.py migrate untuk menerapkan skema model yang telah dibuat ke dalam database Django lokal
4. Menjalankan perintah python manage.py loaddata initial_catalog_data.json untuk memasukkan data tersebut ke dalam database Django lokal.
5. Membuat fungsi show_katalog pada views.py

         def show_katalog(request):
            return render(request, "katalog.html")
      
6. Menambahkan kode urls.py pada folder katalog

         from django.urls import path
         from katalog.views import show_katalog

         app_name = 'katalog'

         urlpatterns = [
            path('', show_katalog, name='show_katalog'),
         ]

7. Menambahkan kode berikut pada katalog.html

        {% for barang in list_barang %}

        <tr>

           <th>{{barang.item_name}}</th>

           <th>{{barang.item_price}}</th>

           <th>{{barang.item_stock}}</th>

           <th>{{barang.description}}</th>

           <th>{{barang.rating}}</th>

           <th>{{barang.item_url}}</th>

        </tr>

8. Mendaftarkan aplikasi katalog ke dalam urls.py yang ada pada folder project_django dengan menambahkan potongan kode berikut pada variabel urlpatterns

         path('katalog', include('katalog.urls')),
   
   
9. meng-import models yang sudah dibuat ke dalam views.py

         from katalog.models import CatalogItem

10. Menambahkan potongan kode berikut pada fungsi show_katalog

          data_barang_katalog = CatalogItem.objects.all()
          context = {
              'list_barang': data_barang_katalog,
              'nama': 'Fahmi Sabila Firdaus'
          }
    
11. Menambahkan context sebagai parameter ketiga pada return statement fungsi show_katalog. Data yang ada pada variabel context tersebut akan ikut di-render oleh Django sehingga nantinya dapat memunculkan data tersebut pada halaman HTML.

         return render(request, "katalog.html", context)
   
12. Melakukan add, commit, dan push perubahan yang sudah dilakukan untuk menyimpannya ke dalam repositori GitHub pribadi.
13. Menambah aplikasi baru pada Heroku
14. Menyalin API key dari akun Heroku
15. Menambah variabel repository secret baru untuk melakukan deployment, dengan HEROKU_API_KEY dari API key yang tadi sudah disalin, dan HEROKU_API_NAME dari nama aplikasi Heroku yang sudah dibuat sebelumnya
16. Membuka tab GitHub Actions dan jalankan kembali workflow yang gagal
