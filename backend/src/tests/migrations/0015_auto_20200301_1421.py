# Generated by Django 3.0.3 on 2020-03-01 11:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0014_auto_20191226_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testresult',
            name='finishTime',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 1, 14, 21, 27, 18135)),
        ),
    ]
