from django.urls import path

from . import views

app_name = 'market'

urlpatterns = [
    path('',views.index, name='index'),
    path('<int:item_id>/', views.result, name='result'),
]
