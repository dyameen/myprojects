# Generated by Django 3.2.15 on 2022-09-20 08:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('att_sys', '0012_alter_attendance_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(default=datetime.date(2022, 9, 20)),
        ),
    ]
