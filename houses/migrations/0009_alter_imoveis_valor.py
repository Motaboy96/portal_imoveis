# Generated by Django 5.1.4 on 2025-03-19 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0008_alter_imoveisimagem_imovel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imoveis',
            name='valor',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True),
        ),
    ]
