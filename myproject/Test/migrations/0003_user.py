# Generated by Django 3.0.4 on 2020-09-25 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Test', '0002_auto_20200926_0214'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('surname', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=250)),
            ],
        ),
    ]
