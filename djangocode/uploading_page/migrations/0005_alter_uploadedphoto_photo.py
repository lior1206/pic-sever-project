# Generated by Django 5.0.4 on 2024-06-03 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploading_page', '0004_alter_uploadedphoto_photo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadedphoto',
            name='photo',
            field=models.ImageField(upload_to='photos/'),
        ),
    ]
