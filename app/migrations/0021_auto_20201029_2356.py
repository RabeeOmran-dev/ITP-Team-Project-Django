# Generated by Django 3.1.2 on 2020-10-29 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_auto_20201029_2355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertising',
            name='year',
            field=models.CharField(blank=True, choices=[(1, 'الأولى'), (2, 'الثانية'), (3, 'الثالثة'), (4, 'الرابعة'), (5, 'الخامسة')], max_length=20, null=True),
        ),
    ]
