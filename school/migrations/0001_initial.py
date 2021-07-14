# Generated by Django 3.2.2 on 2021-07-01 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('roll_no', models.IntegerField(unique=True)),
                ('city', models.CharField(max_length=50)),
                ('marks', models.IntegerField()),
                ('passed_out', models.DateField()),
            ],
        ),
    ]