from django.db import models

# Create your models here.
class Data(models.Model):
    rekam = models.CharField(max_length=350)
    nama = models.CharField(max_length=350)
    alamat = models.TextField(blank=True,null=True)

    GENDER = (
        ('P', 'Perempuan'),
        ('L', 'Laki-laki')
    )

    gender = models.CharField(max_length=1, choices=GENDER)
    tanggal_lahir = models.DateField()
    dokter = models.CharField(max_length=350)
    departemen = models.CharField(max_length=450)
    diagnosa = models.CharField(max_length=450)
    nomor_ruangan = models.IntegerField()
    jam = models.DurationField()
    tindakan = models.CharField(max_length=350)
    keterangan = models.CharField(max_length=450)

    def __str__(self) -> str:
        return self.nama
