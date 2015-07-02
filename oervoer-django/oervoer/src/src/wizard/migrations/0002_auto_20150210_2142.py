# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wizard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=10, choices=[(b'PRE', b'PRE'), (b'DELIVERED', b'DELIVERED')])),
                ('date', models.DateField()),
                ('brief', models.TextField()),
                ('order', models.ForeignKey(to='wizard.Order')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PickList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField(default=1)),
                ('delivery', models.ForeignKey(to='wizard.Delivery')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('sku', models.CharField(max_length=20)),
                ('qty', models.IntegerField()),
                ('shelf', models.CharField(max_length=20, choices=[(b'BINNENCELL', b'Binnencell'), (b'BUITENCELL', b'Buitencell'), (b'ORGAANBANK', b'OrgaanBank'), (b'PARIS', b'Paris')])),
                ('weight', models.DecimalField(max_digits=10, decimal_places=3)),
                ('verpakking', models.IntegerField(default=1)),
                ('kat_hond', models.CharField(max_length=10, choices=[(b'KAT', b'KAT'), (b'HOND', b'HOND'), (b'KAT&HOND', b'Beide')])),
                ('smaak', models.ForeignKey(to='wizard.Taste')),
                ('vlees', models.ForeignKey(to='wizard.MeatType')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='picklist',
            name='product',
            field=models.ForeignKey(to='wizard.Product'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='globals',
            name='BOTFACTOR',
            field=models.FloatField(default=0.1575),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='globals',
            name='DESC',
            field=models.CharField(default='standard', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='globals',
            name='KARKASFACTOR',
            field=models.FloatField(default=0.35),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='globals',
            name='ORGAANFACTOR',
            field=models.FloatField(default=0.0525),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='globals',
            name='PENSFACTOR',
            field=models.FloatField(default=0.15),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='globals',
            name='REPEATS',
            field=models.IntegerField(default=80),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='globals',
            name='SPIERFACTOR',
            field=models.FloatField(default=0.13999999999999999),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='globals',
            name='VISFACTOR',
            field=models.FloatField(default=0.15),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(default='ACTIVE', max_length=10, choices=[(b'PENDING', b'Pending'), (b'COMPLETED', b'Completed'), (b'ACTIVE', b'Active')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='globals',
            name='TESTENV',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='meattype',
            name='is_bot',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='meattype',
            name='is_fish',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='meattype',
            name='is_karkas',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='meattype',
            name='is_orgaan',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='meattype',
            name='is_pens',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='meattype',
            name='is_spier',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='paid',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pet',
            name='weight',
            field=models.DecimalField(max_digits=5, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='taste',
            name='is_big',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='taste',
            name='is_else',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='taste',
            name='is_fish',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='taste',
            name='is_fishhead',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='taste',
            name='is_fowl',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='taste',
            name='is_liver',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='taste',
            name='is_organ',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='taste',
            name='is_small',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
