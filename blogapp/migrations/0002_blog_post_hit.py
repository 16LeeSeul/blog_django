# Generated by Django 2.1.5 on 2019-02-16 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='post_hit',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
