# Generated by Django 2.2.5 on 2019-10-04 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='item',
            new_name='item_id',
        ),
        migrations.AlterField(
            model_name='choice',
            name='pub_date',
            field=models.DateField(verbose_name='Date published'),
        ),
    ]
