# Generated by Django 2.1.4 on 2019-03-01 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CollectionState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('state_description', models.CharField(max_length=150)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DocumentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('description', models.CharField(max_length=150)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GuaranteeDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('payment_date', models.DateField()),
                ('payment_amount', models.DecimalField(decimal_places=5, default=0, max_digits=20)),
                ('external_id', models.CharField(max_length=150)),
                ('external_operation_id', models.CharField(max_length=150)),
                ('fines', models.DecimalField(decimal_places=5, default=0, max_digits=20)),
                ('document_description', models.CharField(max_length=150)),
                ('document_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='collection_module.DocumentType')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Payer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=150)),
                ('external_id', models.CharField(max_length=150)),
                ('contact_data', models.CharField(max_length=150)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('amount', models.DecimalField(decimal_places=5, default=0, max_digits=20)),
                ('payment_payer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='collection_module.Payer')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='guaranteedocument',
            name='payer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='collection_module.Payer'),
        ),
        migrations.AddField(
            model_name='guaranteedocument',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='collection_module.CollectionState'),
        ),
    ]
