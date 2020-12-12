# Generated by Django 3.1.3 on 2020-12-05 20:09

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import veems.common.fields
import veems.media.models
import veems.media.storage_backends


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                (
                    'id',
                    veems.common.fields.ShortUUIDField(
                        default=veems.common.fields._default,
                        editable=False,
                        max_length=12,
                        primary_key=True,
                        serialize=False
                    )
                ),
                (
                    'created_on',
                    models.DateTimeField(auto_now_add=True, db_index=True)
                ),
                (
                    'modified_on',
                    models.DateTimeField(auto_now=True, db_index=True)
                ),
                ('presigned_upload_url', models.URLField()),
                ('media_type', models.CharField(max_length=200)),
                (
                    'file',
                    models.FileField(
                        storage=veems.media.storage_backends.UploadStorage,
                        upload_to=veems.media.models._upload_file_upload_to
                    )
                ),
            ],
            options={
                'ordering': ['created_on'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                (
                    'id',
                    veems.common.fields.ShortUUIDField(
                        default=veems.common.fields._default,
                        editable=False,
                        max_length=12,
                        primary_key=True,
                        serialize=False
                    )
                ),
                (
                    'created_on',
                    models.DateTimeField(auto_now_add=True, db_index=True)
                ),
                (
                    'modified_on',
                    models.DateTimeField(auto_now=True, db_index=True)
                ),
                ('title', models.CharField(max_length=500)),
                (
                    'visibility',
                    models.CharField(
                        choices=[
                            ('private', 'private'), ('public', 'public'),
                            ('unlisted', 'unlisted')
                        ],
                        max_length=10
                    )
                ),
                ('description', models.TextField(max_length=5000)),
                (
                    'tags',
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=1000),
                        null=True,
                        size=None
                    )
                ),
                (
                    'upload',
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to='media.upload'
                    )
                ),
            ],
            options={
                'ordering': ['created_on'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TranscodeJob',
            fields=[
                (
                    'id',
                    veems.common.fields.ShortUUIDField(
                        default=veems.common.fields._default,
                        editable=False,
                        max_length=12,
                        primary_key=True,
                        serialize=False
                    )
                ),
                (
                    'created_on',
                    models.DateTimeField(auto_now_add=True, db_index=True)
                ),
                (
                    'modified_on',
                    models.DateTimeField(auto_now=True, db_index=True)
                ),
                ('profile', models.CharField(max_length=100)),
                ('executor', models.CharField(max_length=20)),
                (
                    'status',
                    models.CharField(
                        choices=[
                            ('created', 'created'),
                            ('processing', 'processing'),
                            ('completed', 'completed'), ('failed', 'failed')
                        ],
                        max_length=10
                    )
                ),
                ('started_on', models.DateTimeField(db_index=True, null=True)),
                ('ended_on', models.DateTimeField(db_index=True, null=True)),
                (
                    'video',
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to='media.video'
                    )
                ),
            ],
            options={
                'ordering': ['created_on'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MediaFile',
            fields=[
                (
                    'id',
                    veems.common.fields.ShortUUIDField(
                        default=veems.common.fields._default,
                        editable=False,
                        max_length=12,
                        primary_key=True,
                        serialize=False
                    )
                ),
                (
                    'created_on',
                    models.DateTimeField(auto_now_add=True, db_index=True)
                ),
                (
                    'modified_on',
                    models.DateTimeField(auto_now=True, db_index=True)
                ),
                (
                    'file',
                    models.FileField(
                        storage=veems.media.storage_backends.MediaFileStorage,
                        upload_to=veems.media.models._mediafile_upload_to
                    )
                ),
                ('width', models.IntegerField(null=True)),
                ('height', models.IntegerField(null=True)),
                ('framerate', models.IntegerField(null=True)),
                ('name', models.CharField(max_length=30)),
                ('ext', models.CharField(max_length=4)),
                ('audio_codec', models.CharField(max_length=50, null=True)),
                ('video_codec', models.CharField(max_length=50, null=True)),
                ('container', models.CharField(max_length=30, null=True)),
                ('filesize', models.IntegerField()),
                (
                    'video',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='media.video'
                    )
                ),
            ],
            options={
                'ordering': ['created_on'],
                'abstract': False,
            },
        ),
    ]