# Generated by Django 4.1.3 on 2022-12-12 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProductApp', '0003_urunozellik'),
    ]

    operations = [
        migrations.RenameField(
            model_name='urunimg',
            old_name='UrunID',
            new_name='UrunImages',
        ),
    ]
