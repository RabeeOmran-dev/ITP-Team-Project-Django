# Generated by Django 3.1.2 on 2020-10-19 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20201019_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, null=True),
        ),
    ]
