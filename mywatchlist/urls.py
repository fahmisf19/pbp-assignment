from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from mywatchlist.views import show_mywatchlist, show_mywatchlist_xml, show_mywatchlist_json, show_mywatchlist_data

app_name = 'mywatchlist'

urlpatterns = [
    path('html/', show_mywatchlist, name='show_mywatchlist'),
    path('xml/', show_mywatchlist_xml, name='show_mywatchlist_xml'),
    path('json/', show_mywatchlist_json, name='show_mywatchlist_json'),
    path('json/<int:id>', show_mywatchlist_data, name='show_mywatchlist_data')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)