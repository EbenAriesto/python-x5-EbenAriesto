class Karyawan:
    jumlah_karyawan = 0

    def __init__(self, nama, gaji, usia, alamat):
        self.nama = nama
        self.gaji = gaji
        self.usia = usia
        self.alamat = alamat
        Karyawan.jumlah_karyawan += 1

    def tampilkan_jumlah(self):
        print("Total karyawan:", Karyawan.jumlah_karyawan)
    
    def tampilkan_profil(self):
        print("Nama:", self.nama)
        print("Gaji:", self.gaji)
        print("Usia:", self.usia)
        print("Alamat:", self.alamat)

karyawan1 = Karyawan("Alvin", 1000000, 23, "Notoprajan")
karyawan2 = Karyawan("Billy", 1500000, 29, "Panembahan")
karyawan3 = Karyawan("Charles", 2000000, 31, "Terban")

karyawan1.tampilkan_profil()
karyawan3.tampilkan_profil()
print("Total karyawan:", Karyawan.jumlah_karyawan)