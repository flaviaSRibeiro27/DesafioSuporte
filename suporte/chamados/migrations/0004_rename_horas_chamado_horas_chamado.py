# Generated by Django 4.0.4 on 2022-05-16 02:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chamados', '0003_alter_chamado_horas'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chamado',
            old_name='horas',
            new_name='horas_chamado',
        ),
    ]