# Generated by Django 4.2.7 on 2023-11-19 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guestbook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_first_name', models.CharField(max_length=30)),
                ('user_last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('feedback_frame', models.CharField(max_length=1000)),
                ('checkbox', models.BooleanField(default=False)),
            ],
        ),
    ]
