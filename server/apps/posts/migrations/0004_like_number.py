# Generated by Django 4.1.5 on 2023-02-07 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_ingredient'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='number',
            field=models.IntegerField(default=0),
        ),
    ]