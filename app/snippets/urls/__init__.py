from .api_view import *
from django.urls import include

app_name = 'snippets'
urlpatterns = [
    path('api-view/', include('snippets.urls.api_view')),
]
