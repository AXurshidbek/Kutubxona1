# Generated by Django 4.2.5 on 2023-10-20 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kutubxonaapp', '0002_rename_qayatrish_sana_record_qaytarish_sana'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kitob',
            name='janr',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='talaba',
            name='kitob_soni',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
