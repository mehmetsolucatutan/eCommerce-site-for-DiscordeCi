# Generated by Django 4.1.3 on 2022-12-28 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0011_siparis_siparisadresalici_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siparis',
            name='SiparisADRESALICI',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='siparis',
            name='SiparisADRESALICIGSM',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='siparis',
            name='SiparisADRESALICITC',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='siparis',
            name='SiparisADRESBASLIK',
            field=models.CharField(max_length=50),
        ),
    ]
