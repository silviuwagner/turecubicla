# Generated by Django 2.0.6 on 2018-06-06 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='location',
            field=models.CharField(default='Romania', max_length=50),
        ),
    ]
