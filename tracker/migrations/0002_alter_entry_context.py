# Generated by Django 4.0 on 2022-03-30 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='context',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
