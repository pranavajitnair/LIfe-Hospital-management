# Generated by Django 2.2.5 on 2019-11-28 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Life', '0015_auto_20191128_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='dept',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Life.Department'),
        ),
    ]
