# Generated by Django 4.0.2 on 2022-02-09 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_sites'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sites',
            name='status',
            field=models.BooleanField(),
        ),
    ]