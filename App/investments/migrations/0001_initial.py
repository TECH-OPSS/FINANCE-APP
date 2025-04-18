# Generated by Django 5.0.7 on 2024-07-18 15:56

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
            name='investments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('investment_type', models.CharField(max_length=100)),
                ('amount_invested', models.DecimalField(decimal_places=2, max_digits=10)),
                ('current_value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_invested', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
