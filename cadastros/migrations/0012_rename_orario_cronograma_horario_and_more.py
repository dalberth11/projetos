# Generated by Django 4.2.7 on 2023-11-24 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0011_paciente_idade'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cronograma',
            old_name='orario',
            new_name='horario',
        ),
        migrations.RenameField(
            model_name='medico',
            old_name='detalhes',
            new_name='especificacao',
        ),
    ]