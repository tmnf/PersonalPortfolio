# Generated by Django 2.2.7 on 2019-11-10 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20191109_1922'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('label', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='./main_app/files')),
            ],
        ),
    ]
