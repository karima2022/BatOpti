# Generated by Django 5.1.4 on 2024-12-26 10:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('building', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='building_type',
            field=models.CharField(choices=[('school', 'École'), ('admin', 'Administration'), ('bank', 'Banque'), ('theater', 'Théâtre'), ('cinema', 'Cinéma')], max_length=20),
        ),
        migrations.AlterField(
            model_name='building',
            name='picture',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='building_photos/'),
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('equipment_type', models.CharField(choices=[('elevator', 'Ascenseur'), ('hvac', 'Climatisation'), ('fire_alarm', 'Alarme incendie')], max_length=50)),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipments', to='building.building')),
            ],
        ),
    ]