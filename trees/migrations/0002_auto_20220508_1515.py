# Generated by Django 3.1.3 on 2022-05-08 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trees', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='family',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='specie',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]