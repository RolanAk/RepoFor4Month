# Generated by Django 5.1.4 on 2024-12-10 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='reta',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
