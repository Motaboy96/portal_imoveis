from django.contrib import admin
from . import models  # ou de onde estiver a referência ao seu modelo

# Definindo a classe do Inline para imagens primeiro
class ImoveisImagemInlineAdmin(admin.TabularInline):
    model = models.ImoveisImagem
    extra = 0  # Número de formulários em branco que o admin irá exibir

# Definindo a classe do Admin para imóveis
class ImoveisAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'tipo', 'pretensao', 'descricao', 'cidade', 'bairro', 'rua', 'quartos', 'banheiros', 'vagas_garagem', 'area', 'valor')
    search_fields = ('bairro', 'tipo')
    inlines = [ImoveisImagemInlineAdmin]  # Adicionando o campo de imagens como um inline

# Definindo a classe do Admin para bairros
class BairroAdmin(admin.ModelAdmin):
    list_display = ('bairro',)
    search_fields = ('bairro',)

# Registrando os modelos no admin
admin.site.register(models.Bairros, BairroAdmin)
admin.site.register(models.Imoveis, ImoveisAdmin)

