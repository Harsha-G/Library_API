# Generated by Django 3.2.5 on 2022-08-06 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('author', models.CharField(max_length=30)),
                ('genre', models.CharField(choices=[('HF', 'HISTORICAL FICTION'), ('FA', 'FANTASY'), ('CHL', 'CHILDREN'), ('SCI', 'SCIENCE'), ('SCF', 'SCIENCE FICTION')], max_length=20)),
            ],
        ),
    ]
