# Generated by Django 4.1.3 on 2022-11-21 20:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0002_rename_cpf_perfil_cpf'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='email',
        ),
    ]
