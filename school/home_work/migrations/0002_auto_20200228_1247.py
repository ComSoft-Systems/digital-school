# Generated by Django 3.0 on 2020-02-28 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_work', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home_work',
            name='page',
            field=models.IntegerField(),
        ),
    ]