class Manusia:
    def __init__(self, nama, jk, usia):
        self.nama = nama
        self.jk = jk
        self.usia = usia
    
    def info(self):
        print("Nama: {}\nJenis Kelamin: {}\nUsia: {}".format(self.nama, self.jk, self.usia))
        print("----------")
    
    def makan(self):
        print("Sedang makan nasi")
        print("----------")

class Pelajar(Manusia):
    def __init__(self, nama, jk, usia, nis, nilai):
        Manusia.__init__(self, nama, jk, usia)
        self.nis = nis
        self.nilai = nilai
    
    def belajar(self):
        print("{} sedang belajar".format(self.nama))
        print("----------")
    
    def makan(self):
        print("{} sedang makan pagi dengan nasi".format(self.nama))
        print("----------")

class Pekerja(Manusia):
    def __init__(self, nama, jk, usia, nip, gaji):
        Manusia.__init__(self, nama, jk, usia)
        self.nip = nip
        self.gaji = gaji
    
    def bekerja(self):
        print("{} sedang bekerja".format(self.nama))
        print("----------")

Rudi = Pelajar("Rudianto", "Laki-laki", 16, "15234", 90)
Wawan = Pekerja("Iwan", "Laki-laki", 29, "1987463", 50000000)

Rudi.info()
Rudi.belajar()
Rudi.makan()
Wawan.info()
Wawan.bekerja()
Wawan.makan()