# Generated by Django 4.1.7 on 2023-02-24 08:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Chat', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Message',
        ),
    ]