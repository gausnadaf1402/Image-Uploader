# Generated by Django 4.1.7 on 2023-03-15 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
