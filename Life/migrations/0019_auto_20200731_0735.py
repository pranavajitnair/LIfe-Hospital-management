# Generated by Django 2.2.5 on 2020-07-31 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Life', '0018_merge_20191129_0505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='dept',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Life.Department'),
        ),
    ]