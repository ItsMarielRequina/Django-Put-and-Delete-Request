from django.urls import path
from .views import TagDetailView

urlpatterns = [
    path('tags/<int:id>/', TagDetailView.as_view(), name='tag-detail'),
]
