# Generated by Django 2.1.4 on 2019-02-25 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0009_remove_batch_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='batch',
            name='date',
        ),
        migrations.RemoveField(
            model_name='journal',
            name='assetType',
        ),
        migrations.RemoveField(
            model_name='journal',
            name='date',
        ),
        migrations.RemoveField(
            model_name='journal',
            name='from_account',
        ),
        migrations.RemoveField(
            model_name='journal',
            name='incomeType',
        ),
        migrations.RemoveField(
            model_name='journal',
            name='to_account',
        ),
        migrations.RemoveField(
            model_name='posting',
            name='date',
        ),
        migrations.DeleteModel(
            name='IncomeType',
        ),
    ]