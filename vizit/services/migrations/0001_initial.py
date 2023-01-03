# Generated by Django 4.1.4 on 2023-01-03 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Addresses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('building', models.CharField(max_length=12)),
                ('room', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=32)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='ServiceCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryName', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serviceName', models.CharField(max_length=64)),
                ('serviceCategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.servicecategory')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.company')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.service')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.addresses')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.company')),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='serviceCategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.servicecategory'),
        ),
    ]
