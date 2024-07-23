# Generated by Django 5.0.6 on 2024-07-23 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(max_length=64, verbose_name='Название')),
                ('author', models.CharField(max_length=64, verbose_name='Автор')),
                ('pub_date', models.DateField(verbose_name='Дата публикации')),
            ],
        ),
    ]