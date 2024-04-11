# Generated by Django 5.0.3 on 2024-03-05 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_rename_contact_estoque'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estoque',
            old_name='created_date',
            new_name='data_retirada',
        ),
        migrations.RenameField(
            model_name='estoque',
            old_name='description',
            new_name='motivo_saida',
        ),
        migrations.RenameField(
            model_name='estoque',
            old_name='first_name',
            new_name='nome',
        ),
        migrations.RenameField(
            model_name='estoque',
            old_name='phone',
            new_name='quantidade',
        ),
        migrations.RemoveField(
            model_name='estoque',
            name='email',
        ),
        migrations.RemoveField(
            model_name='estoque',
            name='last_name',
        ),
    ]
