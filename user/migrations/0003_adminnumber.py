# Generated by Django 4.1.3 on 2022-11-28 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_coupon_couponapplied'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=12)),
            ],
        ),
    ]
