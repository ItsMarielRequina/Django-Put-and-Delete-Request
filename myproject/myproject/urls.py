from django.urls import path, include

urlpatterns = [
    path('api/articles/', include('articles.urls')),
]
