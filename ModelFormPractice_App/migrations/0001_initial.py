# Generated by Django 4.1.6 on 2023-02-01 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('second_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('photo', models.ImageField(upload_to='files/photos')),
                ('gender', models.CharField(choices=[('F', 'FEMALE'), ('M', 'MALE')], max_length=2)),
            ],
            options={
                'db_table': 'Applications',
            },
        ),
    ]