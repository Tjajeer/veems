# Generated by Django 3.1.4 on 2021-01-28 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('channel', '0003_auto_20210128_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='description',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
    ]