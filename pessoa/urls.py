from django.urls import path
from .views import ListaPessoaView, PessoaCreateView

urlpatterns = [
    path('', ListaPessoaView.as_view(), name='pessoa.index'),
    path('novo/', PessoaCreateView.as_view(), name = 'pessoa.novo'),
]