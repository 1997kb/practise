# Generated by Django 3.1.7 on 2021-03-30 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0003_auto_20210330_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='destination',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='flight',
            name='origin',
            field=models.CharField(max_length=64),
        ),
        migrations.DeleteModel(
            name='Airport',
        ),
    ]
