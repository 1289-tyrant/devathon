# Generated by Django 3.1.1 on 2020-10-03 06:45

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mess_name', models.CharField(default='Ganga', max_length=4096)),
                ('breakfast_rate', models.IntegerField(default=0)),
                ('lunch_rate', models.IntegerField(default=0)),
                ('dinner_rate', models.IntegerField(default=0)),
                ('extras_rate_breakfast', models.IntegerField(default=0)),
                ('extras_rate_lunch', models.IntegerField(default=0)),
                ('extras_rate_dinner', models.IntegerField(default=0)),
                ('date', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='Warden',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=4096)),
                ('warden_id', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=4096)),
                ('student_id', models.CharField(max_length=20)),
                ('year', models.IntegerField(default=1)),
                ('total_bill', models.IntegerField(default=0)),
                ('mess', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mess.mess')),
            ],
        ),
        migrations.AddField(
            model_name='mess',
            name='warden_id',
            field=models.ForeignKey(default='123456', on_delete=django.db.models.deletion.CASCADE, to='mess.warden'),
        ),
        migrations.CreateModel(
            name='DailyBill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breakfast', models.BooleanField(default=False)),
                ('lunch', models.BooleanField(default=False)),
                ('dinner', models.BooleanField(default=False)),
                ('extras_breakfast', models.IntegerField(default=0)),
                ('extras_lunch', models.IntegerField(default=0)),
                ('extras_dinner', models.IntegerField(default=0)),
                ('date', models.DateField(default=datetime.date.today)),
                ('update', models.BooleanField(default=False)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mess.student')),
            ],
        ),
    ]
