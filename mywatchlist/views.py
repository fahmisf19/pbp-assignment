from django.shortcuts import render
from mywatchlist.models import WatchlistItem
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_mywatchlist(request):
    watchlist_movie = WatchlistItem.objects.all()

    mes = ""
    yes = 0
    no = 0

    for i in range(len(watchlist_movie)) :
        if (watchlist_movie[i].watched == "yes") :
            yes += 1
        else :
            no += 1

    if (yes >= no) :
        mes = "Selamat, kamu sudah banyak menonton!"
    else :
        mes = "Wah, kamu masih sedikit menonton!"

    context = {
        'movie_list': watchlist_movie,
        'nama': 'Fahmi Sabila Firdaus',
        'message' : mes
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


