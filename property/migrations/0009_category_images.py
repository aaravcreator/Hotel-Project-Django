# Generated by Django 3.0.5 on 2020-05-06 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_reserve'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='images',
            field=models.ImageField(null=True, upload_to='category/'),
        ),
    ]