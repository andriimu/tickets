# Generated by Django 5.0.6 on 2024-05-31 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Naming')),
                ('anons', models.CharField(max_length=250, verbose_name='Anounce')),
                ('full_text', models.TextField(verbose_name='textforanoun')),
                ('date', models.DateTimeField(verbose_name='Date of Publication')),
            ],
        ),
    ]
