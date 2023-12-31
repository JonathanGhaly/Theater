# Generated by Django 4.2.5 on 2023-09-07 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seats', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='seat',
            name='COL',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], default='1', max_length=10),
        ),
        migrations.AlterField(
            model_name='seat',
            name='status',
            field=models.CharField(choices=[('available', 'Available'), ('selected', 'Selected'), ('reserved', 'Reserved')], default='available', max_length=10),
        ),
    ]
