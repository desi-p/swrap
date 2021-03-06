# Generated by Django 4.0.3 on 2022-03-16 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certification_name', models.TextField()),
                ('certification_provider', models.TextField()),
                ('date_earned', models.DateField(auto_now_add=True)),
                ('expiration_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.TextField()),
                ('course_provider', models.TextField()),
                ('course_completed', models.BooleanField()),
                ('certificate_earned', models.TextField()),
            ],
        ),
    ]
