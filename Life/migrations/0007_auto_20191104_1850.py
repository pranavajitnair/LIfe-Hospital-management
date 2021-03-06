# Generated by Django 2.2.5 on 2019-11-04 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Life', '0006_auto_20191104_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='password',
            field=models.CharField(default='xyz', max_length=64),
        ),
        migrations.AddField(
            model_name='patient',
            name='password',
            field=models.CharField(default='xyz', max_length=50),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='dept',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Life.Department'),
        ),
    ]
