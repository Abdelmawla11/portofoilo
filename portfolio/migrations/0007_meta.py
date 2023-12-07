# Generated by Django 4.2.7 on 2023-12-06 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_alter_me_intro'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('description', models.TextField(max_length=2500)),
                ('icon', models.ImageField(upload_to='icon')),
            ],
        ),
    ]