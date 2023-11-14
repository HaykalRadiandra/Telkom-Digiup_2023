from person import Person

class Siswa(Person):
    def __init__(self, nama, alamat, nim):
        super().__init__(nama, alamat)
        self.nim = nim

    def tampil(self):
        print('nama=', self.nama, 'alamat=', self.alamat, "nim=", self.nim)