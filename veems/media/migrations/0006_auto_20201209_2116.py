# Generated by Django 3.1.3 on 2020-12-09 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0005_transcodejob_failure_context'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transcodejob',
            name='failure_context',
            field=models.TextField(null=True),
        ),
    ]