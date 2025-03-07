# Generated by Django 5.1.1 on 2024-10-23 14:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_complated', models.BooleanField(default=False, verbose_name='Статус транзакции')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('amount', models.IntegerField(verbose_name='Кол-во Coins')),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_user', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Транзакии',
                'verbose_name_plural': 'Транзакцию',
            },
        ),
    ]
