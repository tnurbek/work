# Generated by Django 3.1.6 on 2021-02-27 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_log'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='file',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]