# Generated by Django 4.0.3 on 2022-03-22 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItunesApple',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('genres', models.CharField(blank=True, max_length=50, null=True)),
                ('price', models.PositiveIntegerField()),
                ('artistName', models.CharField(blank=True, max_length=35, null=True)),
                ('artistId', models.PositiveBigIntegerField()),
            ],
        ),
    ]
