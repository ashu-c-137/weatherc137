# Generated by Django 2.2.6 on 2019-10-20 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='name',
            field=models.CharField(default=' ', max_length=25),
        ),
    ]
