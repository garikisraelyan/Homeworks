# Generated by Django 3.0.4 on 2020-04-04 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Person', '0002_auto_20200404_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
