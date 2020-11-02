# Generated by Django 2.2.2 on 2020-11-01 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Address', models.TextField()),
                ('Email', models.EmailField(max_length=254)),
                ('Contact', models.BigIntegerField()),
                ('Registration_Id', models.IntegerField()),
                ('Status', models.BooleanField(default=False)),
                ('Password', models.CharField(max_length=15)),
                ('Date', models.DateField()),
            ],
        ),
    ]
