# Generated by Django 3.0.2 on 2020-02-06 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_country_country_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_url',
            field=models.ImageField(default='/images/test1.jpg', upload_to='images/'),
        ),
    ]
