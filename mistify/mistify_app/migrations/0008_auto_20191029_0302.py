# Generated by Django 2.2.6 on 2019-10-29 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mistify_app', '0007_auto_20191029_0209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='image',
            field=models.URLField(null=True),
        ),
    ]