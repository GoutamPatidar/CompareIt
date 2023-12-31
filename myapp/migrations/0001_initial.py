# Generated by Django 4.2.3 on 2023-07-28 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='profile_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(default='', max_length=50)),
                ('Mobile', models.CharField(default='', max_length=50)),
                ('Email', models.EmailField(default='', max_length=50)),
                ('Age', models.IntegerField()),
                ('Address', models.CharField(default='', max_length=200)),
                ('Password', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(default='', max_length=254)),
                ('Username', models.CharField(default='', max_length=50)),
                ('Product_name', models.CharField(default='', max_length=50)),
                ('DateTime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
