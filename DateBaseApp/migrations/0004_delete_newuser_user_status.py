# Generated by Django 5.1.4 on 2025-02-16 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DateBaseApp', '0003_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='NewUser',
        ),
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.CharField(default='user', max_length=4),
        ),
    ]
