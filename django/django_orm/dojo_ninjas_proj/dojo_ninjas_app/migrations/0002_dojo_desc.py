# Generated by Django 3.2.3 on 2021-07-14 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='desc',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
