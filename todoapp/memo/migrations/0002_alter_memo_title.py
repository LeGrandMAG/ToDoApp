# Generated by Django 4.0.3 on 2022-03-15 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memo',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
