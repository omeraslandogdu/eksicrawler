# Generated by Django 2.2.5 on 2020-02-11 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EksiModel',
            fields=[
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('status', models.IntegerField(choices=[(1, 'Active'), (0, 'Passive'), (-1, 'Deleted'), (2, 'Waiting')], default=1)),
                ('author', models.CharField(max_length=255)),
                ('url', models.URLField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
