# Generated by Django 4.0.4 on 2022-05-18 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='FirstName LastName', max_length=250)),
                ('email', models.EmailField(default='employee@email.com', max_length=250)),
                ('departament', models.CharField(default='Full-Stack', max_length=250)),
                ('salary', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('birth_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
