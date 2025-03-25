from django.shortcuts import render
from houses.models import Imoveis
from django.db.models import Q
from django.views.generic import ListView
from django.views.generic import DetailView




class ImoveisListView(ListView):
    model = Imoveis
    template_name = 'houses.html'
    context_object_name = 'imoveis'

    def get_queryset(self):
        # queryset = Imoveis.objects.all().order_by('bairro')
        queryset = super().get_queryset().order_by('bairro')

        search = self.request.GET.get('search')
        pretensao = self.request.GET.get('pretensao')
        tipo = self.request.GET.get('tipo')

        if search:
            queryset = queryset.filter(
                Q(bairro__bairro__icontains=search) |
                Q(cidade__icontains=search)
            )

        if pretensao:
            queryset = queryset.filter(pretensao=pretensao)

        if tipo:
            queryset = queryset.filter(tipo=tipo)


        return queryset


class ImoveisRentListView(ListView):
    model = Imoveis
    template_name = 'houses_rent.html'
    context_object_name = 'imoveis_rent'

    def get_queryset(self):
        # Filtra imóveis com 'pretensao' igual a 'Aluguel'
        queryset = Imoveis.objects.filter(pretensao='Aluguel')

        # Captura os parâmetros de filtro
        tipo = self.request.GET.get('tipo')
        search = self.request.GET.get('search')

        # Aplica o filtro de 'search' (bairro, cidade ou condominio)
        if search:
            queryset = queryset.filter(
                Q(bairro__bairro__icontains=search) |  # Buscar no bairro
                Q(cidade__icontains=search) |         # Buscar na cidade
                Q(condominio__icontains=search)       # Buscar no condomínio (se esse campo existir no modelo)
            )

        # Aplica o filtro de 'tipo' (Apartamento, Casa, etc.)
        if tipo:
            queryset = queryset.filter(tipo=tipo)

        # Retorna o queryset filtrado
        return queryset



class ImoveisDetailView(DetailView):
    model = Imoveis
    template_name = 'imovel_detail.html'
    




