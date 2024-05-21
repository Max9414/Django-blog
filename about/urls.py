from . import views
from django.urls import path
urlpatterns = [
    path('about/', views.PostList.as_view(), name='about'),
]