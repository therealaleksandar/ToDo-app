# Generated by Django 2.1.2 on 2018-10-13 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planeri', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='planer',
            name='zavrsen',
            field=models.BooleanField(default=False),
        ),
    ]