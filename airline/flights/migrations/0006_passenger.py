# Generated by Django 3.1.7 on 2021-04-02 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0005_auto_20210330_1400'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=64)),
                ('last', models.CharField(max_length=64)),
                ('flights', models.ManyToManyField(blank=True, related_name='passengers', to='flights.Flight')),
            ],
        ),
    ]
