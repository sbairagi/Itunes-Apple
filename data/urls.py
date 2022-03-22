from django.urls import path
from .views import Index, ShowData

urlpatterns = [
    path('', Index, name="index"),
    path('showdata/', ShowData, name='showdata')
]