# Generated by Django 3.2.6 on 2021-09-12 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('valdivia', '0002_auto_20210912_1526'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150, verbose_name='Nombre de categoria')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'db_table': 'Categoria',
                'ordering': ['id'],
            },
        ),
    ]
