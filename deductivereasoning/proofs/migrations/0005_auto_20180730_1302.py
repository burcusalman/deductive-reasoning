# Generated by Django 2.0.7 on 2018-07-30 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proofs', '0004_auto_20180729_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proof',
            name='type',
            field=models.CharField(default='', max_length=5),
        ),
    ]