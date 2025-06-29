# Generated by Django 5.2.3 on 2025-06-15 17:33

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('ciutat', models.CharField(max_length=100)),
                ('fundacio', models.IntegerField(null=True)),
                ('escut', models.ImageField(blank=True, null=True, upload_to='escuts/')),
            ],
        ),
        migrations.CreateModel(
            name='Lliga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('temporada', models.CharField(max_length=20)),
                ('data_inici', models.DateField(null=True)),
                ('data_fi', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('cognoms', models.CharField(max_length=100)),
                ('data_naixement', models.DateField()),
                ('nacionalitat', models.CharField(max_length=50)),
                ('dorsal', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(99)])),
                ('posicio', models.CharField(max_length=50)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='fotos_jugadors/')),
                ('equip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jugadors', to='futbol.equip')),
            ],
        ),
        migrations.AddField(
            model_name='equip',
            name='lliga',
            field=models.ManyToManyField(related_name='equips', to='futbol.lliga'),
        ),
        migrations.CreateModel(
            name='Partit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField()),
                ('finalitzat', models.BooleanField(default=False)),
                ('lliga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partits', to='futbol.lliga')),
                ('local', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partits_local', to='futbol.equip')),
                ('visitant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partits_visitant', to='futbol.equip')),
            ],
            options={
                'verbose_name_plural': 'partits',
                'ordering': ['data'],
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temps', models.TimeField()),
                ('tipus', models.CharField(choices=[('GOL', 'Gol'), ('AUTOGOL', 'Autogol'), ('FALTA', 'Falta'), ('PENALTY', 'Penalty'), ('MANS', 'Mans'), ('CESSIO', 'Cessió'), ('ENTRADA', 'Entrada'), ('SORTIDA', 'Sortida'), ('TARGETA_GROGA', 'Targeta Groga'), ('TARGETA_VERMELLA', 'Targeta Vermella')], max_length=30)),
                ('detalls', models.TextField(blank=True, null=True)),
                ('equip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='futbol.equip')),
                ('jugador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='futbol.jugador')),
                ('partit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='futbol.partit')),
            ],
        ),
    ]
