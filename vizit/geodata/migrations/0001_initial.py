# Generated by Django 4.1.4 on 2023-01-07 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('tag', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('tag', models.CharField(max_length=2)),
                ('main_language', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='geodata.language')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('building', models.CharField(max_length=12)),
                ('room', models.CharField(max_length=5)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geodata.country')),
            ],
        ),
    ]
