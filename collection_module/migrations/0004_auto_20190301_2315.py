# Generated by Django 2.1.4 on 2019-03-01 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection_module', '0003_auto_20190301_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payer',
            name='external_id',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
