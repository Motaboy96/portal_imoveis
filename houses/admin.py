from django.contrib import admin
from . import models  


class ImoveisImagemInlineAdmin(admin.TabularInline):
    model = models.ImoveisImagem
    extra = 0  


class ImoveisAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'tipo', 'pretensao', 'descricao', 'cidade', 'bairro', 'rua', 'quartos', 'banheiros', 'vagas_garagem', 'area', 'valor')
    search_fields = ('bairro', 'tipo')
    inlines = [ImoveisImagemInlineAdmin]  


class BairroAdmin(admin.ModelAdmin):
    list_display = ('bairro',)
    search_fields = ('bairro',)


admin.site.register(models.Bairros, BairroAdmin)
admin.site.register(models.Imoveis, ImoveisAdmin)

