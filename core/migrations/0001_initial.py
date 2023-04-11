# Generated by Django 4.2 on 2023-04-07 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_name', models.CharField(max_length=59)),
                ('asset_type', models.CharField(max_length=50)),
                ('asset_quantity', models.IntegerField()),
            ],
        ),
    ]