# Generated by Django 2.1.7 on 2019-12-22 12:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0012_auto_20191222_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answerType',
            field=models.CharField(blank=True, choices=[('CH', 'CHOICE'), ('MU', 'CHOICE_MULT'), ('VA', 'VALUE'), ('TE', 'TEXT')], default='TE', max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='testresult',
            name='finishTime',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 22, 15, 32, 42, 591690)),
        ),
    ]
