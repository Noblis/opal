# Generated by Django 3.0.7 on 2020-10-15 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ssp', '0002_auto_20201015_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='hash',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='ssp.hashed_value'),
        ),
    ]