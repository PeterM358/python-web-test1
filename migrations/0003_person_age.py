# Generated by Django 3.2.3 on 2021-05-20 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoStart', '0002_person_home_town'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='age',
            field=models.IntegerField(default=18),
            preserve_default=False,
        ),
    ]