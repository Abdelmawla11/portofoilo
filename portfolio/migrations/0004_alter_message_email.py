# Generated by Django 4.2.7 on 2023-12-02 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_alter_message_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='email',
            field=models.EmailField(max_length=256),
        ),
    ]