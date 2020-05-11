# Generated by Django 3.0.3 on 2020-05-07 02:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parent1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent1_first_name', models.CharField(max_length=100)),
                ('parent1_last_name', models.CharField(max_length=100)),
                ('parent1_email_address', models.EmailField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('child_first_name', models.CharField(max_length=100)),
                ('child_last_name', models.CharField(max_length=100)),
                ('parent1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='covidpolls.Parent1')),
            ],
        ),
    ]
