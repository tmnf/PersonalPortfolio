# Generated by Django 2.2.7 on 2019-11-09 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20191109_1607'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('job_interest', models.CharField(max_length=200)),
                ('birthday', models.DateField()),
                ('biography', models.CharField(max_length=500)),
                ('profile_pic', models.ImageField(upload_to='')),
            ],
        ),
    ]
