# Generated by Django 4.2.6 on 2023-10-26 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='title',
            field=models.CharField(default='Brookhaven Road', max_length=200),
            preserve_default=False,
        ),
    ]