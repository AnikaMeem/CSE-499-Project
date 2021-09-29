# Generated by Django 3.2.4 on 2021-08-06 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('hospital', models.CharField(max_length=100)),
                ('email', models.EmailField(default='', max_length=100, unique=True)),
                ('password', models.CharField(default='', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(default='', max_length=100, unique=True)),
                ('password', models.CharField(default='', max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Appoinment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(default='01/01/1970', max_length=40)),
                ('approved', models.BooleanField(default=False)),
                ('doctor', models.ManyToManyField(related_name='doctor', to='hospital.Doctor')),
                ('patient', models.ManyToManyField(related_name='patient', to='hospital.Patient')),
            ],
        ),
    ]