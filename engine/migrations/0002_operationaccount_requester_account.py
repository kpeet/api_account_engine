# Generated by Django 2.1.4 on 2019-03-27 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='operationaccount',
            name='requester_account',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='requestor', to='engine.Account'),
            preserve_default=False,
        ),
    ]
