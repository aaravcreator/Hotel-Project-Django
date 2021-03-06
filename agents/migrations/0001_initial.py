# Generated by Django 3.0.5 on 2020-04-24 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=30)),
                ('contact', models.IntegerField(max_length=10)),
                ('image', models.ImageField(upload_to='agents/')),
            ],
        ),
    ]
