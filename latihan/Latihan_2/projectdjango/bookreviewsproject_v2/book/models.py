from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Publisher(models.Model):
    nama = models.CharField(max_length=250)
    alamat = models.TextField(blank=True,null=True)
    telpon = models.CharField(blank=True,max_length=10)
    email = models.EmailField(blank=True,null=True)
    def __str__(self) -> str:
        return self.nama

class Book(models.Model):
    judul = models.CharField(max_length=250)
    isbn = models.CharField(max_length=13)
    pengarang = models.CharField(max_length=250)
    sinopsis = models.TextField(blank=True,null=True) #null = DB, blank = form
    tanggal_rilis = models.DateField()
    jumlah_halaman = models.IntegerField()
    gambar = models.ImageField(upload_to='book/images/')
    publisher = models.ForeignKey(Publisher,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.judul