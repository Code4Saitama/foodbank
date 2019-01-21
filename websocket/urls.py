from django.urls import path

from .views import index

from . import views

urlpatterns = [
    # 元のコードは→url(r'^$', views.index, name='index'),
    path('', views.index, name='index'),
    path('<slug:room_name>/', views.room, name='room'),
]
