# Generated by Django 3.1.1 on 2020-09-27 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200927_0318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='nickname',
            field=models.CharField(max_length=100),
        ),
    ]
