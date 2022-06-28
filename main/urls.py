from django.urls import path
from main.views import Homeview

urlpatterns = [
    path('', Homeview.as_view(), name='home')
]