# Generated by Django 2.1.4 on 2019-03-01 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0019_auto_20190301_1342'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='external_account_id',
            field=models.CharField(default=123123, max_length=150),
            preserve_default=False,
        ),
    ]