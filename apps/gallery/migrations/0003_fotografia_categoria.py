# Generated by Django 4.2.4 on 2023-09-18 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_rename_fotos_fotografia_foto_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='categoria',
            field=models.CharField(choices=[('NEBULOSA', 'Nebulosa'), ('ESTRELA', 'Estrela'), ('GALÁXIA', 'Galáxia'), ('SISTEMAS ESTELARES', 'Sistemas Estelares'), ('PLANETAS', 'Planetas')], default='', max_length=100),
        ),
    ]
