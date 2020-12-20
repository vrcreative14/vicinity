# Generated by Django 3.1.2 on 2020-12-17 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0008_auto_20201216_2102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='gstin',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='is_gst_registered',
        ),
        migrations.AddField(
            model_name='storedetails',
            name='gstin',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='storedetails',
            name='is_gst_registered',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='organization',
            name='is_registered',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
