from django.urls import include, path

urlpatterns = [
    path('', include('homepage.urls')),
    path('icecream/', include('icecream.urls')),
]
