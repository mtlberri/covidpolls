# Generated by Django 3.0.3 on 2020-05-15 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covidpolls', '0003_auto_20200510_1534'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParentChildPreference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_first_name', models.CharField(max_length=100)),
                ('parent_last_name', models.CharField(max_length=100)),
                ('parent_email_address', models.EmailField(max_length=200)),
                ('parent_phone', models.CharField(max_length=20)),
                ('child_first_name', models.CharField(max_length=100)),
                ('child_last_name', models.CharField(max_length=100)),
                ('child_return_asap', models.BooleanField()),
                ('child_date_return', models.DateField(blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Child',
        ),
        migrations.DeleteModel(
            name='Parent1',
        ),
    ]