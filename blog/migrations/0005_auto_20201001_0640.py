# Generated by Django 3.1.2 on 2020-10-01 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200613_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='added_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
