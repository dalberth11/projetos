# Generated by Django 5.0 on 2023-12-08 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0019_comentario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentario',
            name='usuario',
        ),
        migrations.AddField(
            model_name='comentario',
            name='nota',
            field=models.IntegerField(default=1, verbose_name='nota'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comentario',
            name='sugestoes',
            field=models.TextField(max_length=255, verbose_name='sugestoes'),
        ),
    ]
