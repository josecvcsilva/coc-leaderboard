# Generated by Django 3.2.24 on 2025-03-03 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wars', '0003_auto_20250302_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='war_player_attack',
            name='opponent_name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
