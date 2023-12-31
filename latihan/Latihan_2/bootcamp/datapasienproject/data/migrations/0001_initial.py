# Generated by Django 4.1.3 on 2023-11-11 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rekam', models.CharField(max_length=350)),
                ('nama', models.CharField(max_length=350)),
                ('alamat', models.TextField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('P', 'Perempuan'), ('L', 'Laki-laki')], max_length=1)),
                ('tanggal_lahir', models.DateField()),
                ('dokter', models.CharField(max_length=350)),
                ('departemen', models.CharField(max_length=450)),
                ('diagnosa', models.CharField(max_length=450)),
                ('nomor_ruangan', models.IntegerField()),
                ('jam', models.DurationField()),
                ('tindakan', models.CharField(max_length=350)),
                ('Keterangan', models.CharField(max_length=450)),
            ],
        ),
    ]
