# Generated by Django 4.0.5 on 2023-01-12 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='get_user_info_one',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('string_email', models.CharField(max_length=50)),
                ('string_phon_number', models.CharField(max_length=11, null=True)),
                ('string_date', models.DateField(blank=True, null=True)),
                ('string_text', models.CharField(max_length=150)),
            ],
        ),
    ]