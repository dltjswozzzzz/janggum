# Generated by Django 4.1.6 on 2023-02-21 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_post_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, default='default.png', upload_to='posts/%Y%m%d'),
        ),
    ]
