# Generated by Django 3.0.2 on 2020-04-05 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20200405_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profile2.jpg', null=True, upload_to=''),
        ),
    ]
