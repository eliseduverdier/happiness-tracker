# Generated by Django 4.0 on 2022-03-30 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_alter_entry_context'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='context',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
