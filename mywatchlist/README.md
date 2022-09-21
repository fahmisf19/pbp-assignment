tautan :

https://pbp-assignment-fahmi.herokuapp.com/mywatchlist/html/

https://pbp-assignment-fahmi.herokuapp.com/mywatchlist/xml/

https://pbp-assignment-fahmi.herokuapp.com/mywatchlist/json/


Jelaskan perbedaan antara JSON, XML, dan HTML!

- JSON atau *JavaScript Object Notation* merupakan sebuah format yang digunakan untuk menyimpan, membaca, serta menukar informasi dari web server sehingga dapat dibaca oleh para pengguna. JSON terdiri dari dua struktur atau bagian. Yang pertama adalah kumpulan value yang saling berpasangan contohnya seperti object. Struktur kedua adalah kumpulan value yang berurutan seperti misalnya array.
- XML atau *Extensible Markup* Language merupakan sebuah markup language yang digunakan untuk menyederhanakan pertukaran dan penyimpanan data. XML memiliki tiga struktur pembentuk, yaitu deklarasi, atribut, dan elemen.
- HTML atau *Hypertext Markup Language* merupakan sebuah markup language yang digunakan untuk membuat halaman website. Isinya terdiri dari berbagai kode yang dapat menyusun struktur suatu website. HTML terdiri dari tiga struktur, yaitu tag, elemen, dan atribut.

Perbedaan antara JSON dan XML :
- JSON menyimpan elemennya secara efisien akan tetapi tidak rapi untuk dilihat. Sedangkan XML menyimpan elemen-elemen nya dengan cara yang terstruktur, mudah dibaca oleh manusia dan mesin, akan tetapi kurang efisien.
- JSON memliki banyak tipe, XML tidak mempunyai tipe.
- JSON tidak menyediakan *namespace*, XML menyediakan *namespace*.
- JSON berekstensi .json, XML berekstensi .xml
- JSON mendukung *array*, XML tidak mendukung *array*.
- JSON hanya mendukung tipe data teks dan angka, XML mendukung teks, angka, gambar, *charts*, *graphs*, dll.

Perbedaan antara XML dan HTML :
- XML berfokus pada transfer data, HTML berfokus pada presentasi data.
- XML *content driven*, HTML *format driven*.
- XML *case sensitive*, HTML *case insensitive*.
- XML mendukung *namespace*, HTML tidak mendukung *namespace*.
- XML tags *extensible*, HTML tags terbatas.

 Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

1.  git clone repositori pada komputer, kemudian membuat virtual environment, dan menyalakan virtual environment tersebut, lalu menginstal semua dependencies yang ada pada requirements.txt

2.  Membuat sebuah django-app bernama mywatchllist dengan perintah
        
        python manage.py startapp wishlist
        
3.  Buka settings.py di folder project_django dan tambahkan aplikasi mywatchlist ke dalam variabel INSTALLED_APPS untuk mendaftarkan django-app dibuat ke dalam proyek Django.

        INSTALLED_APPS = [
        ...,
        'mywatchlist',
        ]
     
4.  Membuka file models.py yang ada di folder wishlist dan menambahkan kode berikut
  
       from django.db import models

       class WatchlistItem(models.Model):
           watched = models.CharField(max_length=50)
           title = models.CharField(max_length=225)
           rating = models.FloatField()
           release_date = models.TextField()
           review = models.TextField()
          
5.  Menjalankan perintah python manage.py makemigrations untuk mempersiapkan migrasi skema model ke dalam database Django lokal.

6.  Menjalankan perintah python manage.py migrate untuk menerapkan skema model yang telah dibuat ke dalam database Django lokal.

7.  Membuat folder fixtures di dalam folder aplikasi mywatchlist dan buatlah sebuah berkas bernama initial_mywatchlist_data.json yang berisi kode berikut.

        [
          {
              "model":"mywatchlist.watchlistitem",
              "pk":1,
              "fields":{
                  "watched":"yes",
                  "title":"The VVitch",
                  "rating": "3.4",
                  "release_date": "October 15th 2015",
                  "review": "Black Phillip GOATED"
              }
                },
                {
                    "model":"mywatchlist.watchlistitem",
                    "pk":2,
                    "fields":{
                        "watched":"yes",
                        "title":"The Wailing",
                        "rating": "3.7",
                        "release_date": "May 26th 2016",
                        "review": "Japanese man goes brrah"
                    }
                },
                {
                    "model":"mywatchlist.watchlistitem",
                    "pk":3,
                    "fields":{
                        "watched":"yes",
                        "title":"Hereditary",
                        "rating": "3.6",
                        "release_date": "June 27th 2018",
                        "review": "Hidden mom in the corner of the ceiling, brr"
                    }
                },
                {
                    "model":"mywatchlist.watchlistitem",
                    "pk":4,
                    "fields":{
                        "watched":"yes",
                        "title":"Midsommar",
                        "rating": "3.5",
                        "release_date": "September 7th 2019",
                        "review": "cry, cry, CRY"
                    }
                },
                {
                    "model":"mywatchlist.watchlistitem",
                    "pk":5,
                    "fields":{
                        "watched":"yes",
                        "title":"Us",
                        "rating": "3.4",
                        "release_date": "September 20th 2019",
                        "review": "Adelaide is not the real Adelaide. Whaa-?"
                    }
                },
                {
                    "model":"mywatchlist.watchlistitem",
                    "pk":6,
                    "fields":{
                        "watched":"yes",
                        "title":"Get Out",
                        "rating": "3.8",
                        "release_date": "March 29th 2017",
                        "review": "The twist tho-"
                    }
                },
                {
                    "model":"mywatchlist.watchlistitem",
                    "pk":7,
                    "fields":{
                        "watched":"no",
                        "title":"X",
                        "rating": "3.3",
                        "release_date": "March 18th 2022",
                        "review": "BOLD horror movie"
                    }
                },
                {
                    "model":"mywatchlist.watchlistitem",
                    "pk":8,
                    "fields":{
                        "watched":"yes",
                        "title":"The Autopsy of Jane Doe",
                        "rating": "3.4",
                        "release_date": "December 26th 2016",
                        "review": "Making us feel that coroner is a cool-not cool job"
                    }
                },
                {
                    "model":"mywatchlist.watchlistitem",
                    "pk":9,
                    "fields":{
                        "watched":"no",
                        "title":"Apollo 18",
                        "rating": "2.6",
                        "release_date": "September 2nd 2011",
                        "review": "Moon is not safe"
                    }
                },
                {
                    "model":"mywatchlist.watchlistitem",
                    "pk":10,
                    "fields":{
                        "watched":"no",
                        "title":"Malignant",
                        "rating": "3.1",
                        "release_date": "October 31st 2021",
                        "review": "Great experimental movie"
                    }
                }
             ]

8.  Menjalankan perintah python manage.py loaddata initial_mywatchlist_data.json untuk memasukkan data tersebut ke dalam database Django lokal.

9.  Membuka views.py yang ada pada folder mywatchlist dan menambahkan kode berikut

        def show_mywatchlist(request):
            watchlist_movie = WatchlistItem.objects.all()
            context = {
                'movie_list': watchlist_movie,
                'nama': 'Fahmi Sabila Firdaus'
            }
            return render(request, "mywatchlist.html", context)
            
         def show_mywatchlist_xml(request):
             data = WatchlistItem.objects.all()
             return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

         def show_mywatchlist_json(request):
             data = WatchlistItem.objects.all()
             return HttpResponse(serializers.serialize("json", data), content_type="application/json")

         def show_mywatchlist_data(request, id):
             data = WatchlistItem.objects.filter(pk=id)
             #  Jika JSON
             return HttpResponse(serializers.serialize("json", data), content_type="application/json")

             #  Jika XML
             # return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
            
10. Membuat sebuah folder bernama templates di dalam folder aplikasi mywatchlist dan membuat sebuah berkas bernama mywatchlist.html. Lalu, menambahkan kode berikut

        {% extends 'base.html' %}

        {% block content %}

         <h1>Assignment 3 PBP/PBD</h1>

         <div class="identity">
           <h5>Name: </h5>
           <p>Fahmi Sabila Firdaus</p>

           <h5>Student ID: </h5>
           <p>2106751745</p>
         </div>


         <table class="content-table">
           <tr class="table-header">
             <th>Watched?</th>
             <th>Title</th>
             <th>Rating</th>
             <th>Release date</th>
             <th>Review</th>
           </tr>
           {% comment %} Add the data below this line {% endcomment %}
           {% for movie in movie_list %}
           <tr>
               <th>{{movie.watched}}</th>
               <th>{{movie.title}}</th>
               <th>{{movie.rating}}</th>
               <th>{{movie.release_date}}</th>
               <th>{{movie.review}}</th>
           </tr>
        {% endfor %}
          </table>
        {% endblock content %}
        
11. Melakukan routing terhadap fungsi views yang telah dibuat sehingga nantinya halaman HTML dapat ditampilkan lewat browser, dengan menambahkan kode berikut pada urls.py.

        from django.urls import path

        from mywatchlist.views import show_mywatchlist, show_mywatchlist_xml, show_mywatchlist_json, show_mywatchlist_data

        app_name = 'mywatchlist'

        urlpatterns = [
            path('html/', show_mywatchlist, name='show_mywatchlist'),
            path('xml/', show_mywatchlist_xml, name='show_mywatchlist_xml'),
            path('json/', show_mywatchlist_json, name='show_mywatchlist_json'),
            path('json/<int:id>', show_mywatchlist_data, name='show_mywatchlist_data')
        ]
        
12. Mendaftarkan aplikasi mywatchlist ke dalam urls.py yang ada pada folder project_django dengan menambahkan potongan kode berikut pada variabel urlpatterns.

        ...
        path('mywatchlist/', include('mywatchlist.urls')),
        ...
      
13. 
