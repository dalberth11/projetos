# Generated by Django 4.2.7 on 2023-12-08 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0015_medico_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='status',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='medico',
            name='cpf',
            field=models.CharField(max_length=11, verbose_name=' cpf '),
        ),
    ]
