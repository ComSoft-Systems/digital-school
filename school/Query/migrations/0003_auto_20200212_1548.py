# Generated by Django 3.0.3 on 2020-02-12 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Query', '0002_auto_20200212_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry_data',
            name='date_of_test',
            field=models.DateField(),
        ),
    ]