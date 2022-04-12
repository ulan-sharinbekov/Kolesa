# Generated by Django 4.0.3 on 2022-04-06 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Models',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('transmission', models.CharField(choices=[('Automatic', 'Automatic'), ('Mechanics', 'Mechanics'), ('Robots', 'Robots')], max_length=200)),
                ('steering', models.CharField(choices=[('Left', 'Left'), ('Right', 'Right')], max_length=200)),
                ('color', models.CharField(max_length=200)),
                ('drive_unit', models.CharField(choices=[('Left', 'Left'), ('Right', 'Right')], max_length=200)),
                ('cleared_RK', models.BooleanField(default=True)),
                ('description', models.TextField(blank=True)),
                ('contacts', models.IntegerField()),
                ('year', models.IntegerField()),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.brand')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.city')),
            ],
        ),
    ]
