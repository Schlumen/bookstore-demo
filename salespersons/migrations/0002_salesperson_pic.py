# Generated by Django 4.2.4 on 2023-09-05 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salespersons', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesperson',
            name='pic',
            field=models.ImageField(default='no_image.jpg', upload_to='salespersons'),
        ),
    ]
