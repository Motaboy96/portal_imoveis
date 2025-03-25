from django.db import models
from django.utils.formats import number_format


class Bairros(models.Model):
    id = models.AutoField(primary_key=True)
    bairro = models.CharField(max_length=200)

    def __str__(self):
        return self.bairro

    class Meta:
        verbose_name = "Bairro"  # Nome no singular
        verbose_name_plural = "Bairros"  # Nome no plural


class Imoveis(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=50, blank=True, null=True)
    tipo = models.CharField(
        max_length=50,
        choices=[
            ("Casa", "Casa"),
            ("Apartamento", "Apartamento"),
            ("Comercial", "Comercial"),
            ("Terreno", "Terreno"),
        ]
    )
    pretensao = models.CharField(
        max_length=50,
        choices=[
            ("Aluguel", "Aluguel"),
            ("Venda", "Venda"),
        ],
        blank=True,  
        null=True    
    )
    descricao = models.TextField(blank=True, null=True)
    cidade = models.CharField(max_length=200)
    bairro = models.ForeignKey(Bairros, on_delete=models.PROTECT, related_name='imovel_bairro')
    rua = models.CharField(max_length=200, blank=True, null=True)
    quartos = models.IntegerField()
    banheiros = models.IntegerField()
    vagas_garagem = models.IntegerField()
    area = models.FloatField(blank=True, null=True)
    valor = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)

    def valor_formatado(self):
        return number_format(self.valor, use_l10n=True)

    
    def __str__(self):
        return f"{self.tipo} em {self.bairro}"

    class Meta:
        verbose_name = "Imovel"  
        verbose_name_plural = "Imoveis" 

class ImoveisImagem(models.Model):
    imagem = models.ImageField("imagens", upload_to='imagens/', blank=True, null=True)
    imovel = models.ForeignKey(Imoveis, on_delete=models.CASCADE, related_name='imovel_imagens')

    def __str__(self):
        return f"Imagem do imovel: {self.imovel.bairro}"
