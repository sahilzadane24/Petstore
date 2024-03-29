# Generated by Django 4.2.6 on 2023-10-26 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='img%y')),
                ('name', models.CharField(max_length=30)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=30)),
                ('species', models.CharField(max_length=30)),
                ('breed', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('description', models.CharField(max_length=500)),
            ],
        ),
    ]
