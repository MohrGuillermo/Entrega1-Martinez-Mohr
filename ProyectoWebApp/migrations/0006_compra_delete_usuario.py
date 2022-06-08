# Generated by Django 4.0.4 on 2022-06-08 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoWebApp', '0005_comentario_texto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('banco', models.CharField(max_length=40)),
                ('paquete', models.CharField(max_length=40)),
                ('nrotarjeta', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]