# Generated by Django 2.2.1 on 2019-05-02 15:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20190502_2115'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 2, 15, 42, 50, 160801, tzinfo=utc), editable=False),
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 2, 15, 43, 55, 21555, tzinfo=utc)),
            preserve_default=False,
        ),
    ]