from django.urls import reverse_lazy
from Desafio.models import Tecnologias, InsereTecnologiaForm
from django.views.generic import ListView, TemplateView, DeleteView, CreateView


class IndexTemplateView(TemplateView):
    template_name = "index.html"
    context_object_name = 'tecnologias'
    model = Tecnologias


class TecnologiasListView(ListView):
    template_name = "index.html"
    model = Tecnologias
    context_object_name = "tecnologias"


class TecnologiasDeleteView(DeleteView):
    template_name = "index.html"
    model = Tecnologias
    context_object_name = 'tecnologias'
    success_url = reverse_lazy("")


class TecnologiaCreateView(CreateView):
    template_name = "index.html"
    model = Tecnologias
    context_object_name = 'tecnologias'
    form_class = InsereTecnologiaForm
    success_url = "localhost/v"
