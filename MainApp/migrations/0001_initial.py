# Generated by Django 4.1.7 on 2023-02-19 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('csv_file', models.FileField(upload_to='documents/')),
                ('time_frame', models.PositiveIntegerField()),
                ('upload_at', models.DateTimeField(auto_now_add=True)),
                ('json_file', models.FileField(blank=True, upload_to='output/')),
            ],
        ),
    ]
