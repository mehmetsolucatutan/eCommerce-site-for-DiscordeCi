# Generated by Django 4.1.3 on 2022-11-28 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0005_alter_user_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='TOKENDATE',
            field=models.DateTimeField(null=True),
        ),
    ]
