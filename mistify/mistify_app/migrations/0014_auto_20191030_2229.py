# Generated by Django 2.2.6 on 2019-10-31 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mistify_app', '0013_auto_20191030_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='datetime',
            field=models.CharField(default='10:29 PM, Oct 3, 2019', max_length=50),
        ),
    ]