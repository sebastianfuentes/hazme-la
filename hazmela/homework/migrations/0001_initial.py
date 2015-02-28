# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=144)),
                ('publishedDate', models.DateTimeField(verbose_name=b'date published')),
                ('document', models.FileField(upload_to=b'documents/%Y/%m/%d')),
                ('status', models.IntegerField()),
                ('dueDate', models.DateTimeField(verbose_name=b'due date')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
