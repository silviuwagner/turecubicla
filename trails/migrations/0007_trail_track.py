# Generated by Django 2.0.6 on 2018-06-17 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trails', '0006_trail_difficulty'),
    ]

    operations = [
        migrations.AddField(
            model_name='trail',
            name='track',
            field=models.FileField(default='tracklink', upload_to='tracks/'),
        ),
    ]
