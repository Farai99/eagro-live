# Generated by Django 3.0.1 on 2021-08-08 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20210807_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
