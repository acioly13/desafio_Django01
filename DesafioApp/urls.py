from django.urls import path
from DesafioApp.views import *

app_name = 'DesafioApp'
# urlpatterns a lista de roteamentos de URLs para funções/Views
urlpatterns = [
    # GET /
    path('v', TecnologiasListView.as_view()),
    path('excluir/<pk>', TecnologiasDeleteView.as_view()),
    path('', TecnologiaCreateView.as_view()),

]
