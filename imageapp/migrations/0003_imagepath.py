# Generated by Django 3.2.7 on 2021-09-21 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageapp', '0002_mlimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagepath',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imname', models.TextField()),
            ],
        ),
    ]
