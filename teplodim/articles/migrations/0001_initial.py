# Generated by Django 3.1.1 on 2020-09-20 11:49

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('content', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('files', django.contrib.postgres.fields.ArrayField(base_field=models.FileField(upload_to='uploads/'), size=None)),
            ],
        ),
    ]