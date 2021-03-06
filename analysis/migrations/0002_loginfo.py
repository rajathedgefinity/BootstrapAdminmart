# Generated by Django 2.2.8 on 2020-01-30 06:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='loginfo',
            fields=[
                ('switchname', models.CharField(max_length=40)),
                ('timestamp', models.DateTimeField(blank=True, default=None, null=True)),
                ('intialvalue', models.BooleanField(blank=True, default=None, null=True)),
                ('finalvalue', models.BooleanField(blank=True, default=None, null=True)),
                ('userid', models.AutoField(primary_key=True, serialize=False)),
                ('hubid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analysis.hubinfo')),
            ],
        ),
    ]
