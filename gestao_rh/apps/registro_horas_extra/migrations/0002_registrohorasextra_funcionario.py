# Generated by Django 2.2.2 on 2019-09-06 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0002_auto_20190906_1606'),
        ('registro_horas_extra', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrohorasextra',
            name='funcionario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='funcionarios.Funcionario'),
            preserve_default=False,
        ),
    ]
