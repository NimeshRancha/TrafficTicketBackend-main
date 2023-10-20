# Generated by Django 4.2.5 on 2023-10-13 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_rename_officer_id_schedule_officer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='day_shift',
        ),
        migrations.AddField(
            model_name='schedule',
            name='shift',
            field=models.CharField(default='day', max_length=5),
            preserve_default=False,
        ),
    ]