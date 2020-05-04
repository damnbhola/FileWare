# Generated by Django 3.0.5 on 2020-04-09 11:11

from django.db import migrations, models
import fileware.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='file')),
                ('file_name', models.CharField(max_length=50)),
                ('up_date', models.DateTimeField()),
                ('location', models.CharField(blank=True, default=fileware.models.at, max_length=8)),
            ],
        ),
    ]