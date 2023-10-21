# Generated by Django 4.2 on 2023-10-20 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0002_alter_producto_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.CharField(choices=[('Comidas', 'Comidas'), ('Cafeteria', 'Cafeteria'), ('Bebidas', 'Bebidas'), ('Platos de Autor', 'Platos de Autor'), ('Opciones rapidas', 'Opciones rapidas'), ('Cocteles y tragos', 'Cocteles y tragos'), ('Whiskeys', 'Whiskeys'), ('Cofee', 'Cofee'), ('Non Cofee', 'Non Cofee'), ('Smoothie', 'Smoothie'), ('Bakery and pastry', 'Bakery and pastry')], max_length=100, verbose_name='categoria'),
        ),
    ]
