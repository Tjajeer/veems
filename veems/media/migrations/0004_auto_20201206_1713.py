# Generated by Django 3.1.3 on 2020-12-06 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0003_mediafile_duration'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mediafile',
            old_name='filesize',
            new_name='file_size',
        ),
    ]