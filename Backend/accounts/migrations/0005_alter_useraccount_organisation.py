# Generated by Django 5.0.4 on 2024-04-28 16:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_useraccount_is_staff_alter_useraccount_is_superuser'),
        ('organisations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='organisation',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='user_accounts', to='organisations.organisation'),
        ),
    ]