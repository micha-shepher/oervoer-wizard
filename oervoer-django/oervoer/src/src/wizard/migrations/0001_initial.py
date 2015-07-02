# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Globals',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('MEALFACTOR', models.FloatField(default=4.0)),
                ('MEALFACTOR2', models.FloatField(default=0.2)),
                ('MEALFACTOR3', models.FloatField(default=1.5)),
                ('CATFACTOR', models.FloatField(default=0.035)),
                ('DOGFACTOR', models.FloatField(default=0.025)),
                ('tries', models.IntegerField(default=10)),
                ('LIKEFACTOR', models.FloatField(default=4.0)),
                ('SMALLMEAL', models.IntegerField(default=250)),
                ('BIGMEAL', models.IntegerField(default=500)),
                ('TESTENV', models.FilePathField(path=b'../test')),
                ('LEVERDEEL', models.FloatField(default=0.4)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MeatType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('meat_type', models.CharField(max_length=30)),
                ('is_fish', models.BooleanField()),
                ('is_pens', models.BooleanField()),
                ('is_spier', models.BooleanField()),
                ('is_orgaan', models.BooleanField()),
                ('is_karkas', models.BooleanField()),
                ('is_bot', models.BooleanField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('paid', models.BooleanField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=10, choices=[(b'COMBI', b'COMBI'), (b'100', b'100%'), (b'PLUS', b'PLUS+')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('weight', models.FloatField()),
                ('factor', models.FloatField(default=1.0)),
                ('owner', models.ForeignKey(to='wizard.Owner')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='prefers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pet', models.ForeignKey(to='wizard.Pet')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ras',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ras', models.CharField(max_length=10, choices=[(b'KAT', b'KAT'), (b'HOND', b'HOND')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Taste',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('taste', models.CharField(max_length=30)),
                ('is_big', models.BooleanField()),
                ('is_small', models.BooleanField()),
                ('is_fish', models.BooleanField()),
                ('is_organ', models.BooleanField()),
                ('is_fowl', models.BooleanField()),
                ('is_else', models.BooleanField()),
                ('is_liver', models.BooleanField()),
                ('is_fishhead', models.BooleanField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='prefers',
            name='taste',
            field=models.ForeignKey(to='wizard.Taste'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pet',
            name='ras',
            field=models.ForeignKey(to='wizard.Ras'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='owner',
            field=models.ForeignKey(to='wizard.Owner'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='package',
            field=models.ForeignKey(to='wizard.Package'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='pet',
            field=models.ForeignKey(to='wizard.Pet'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='donts',
            name='pet',
            field=models.ForeignKey(to='wizard.Pet'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='donts',
            name='taste',
            field=models.ForeignKey(to='wizard.Taste'),
            preserve_default=True,
        ),
    ]
