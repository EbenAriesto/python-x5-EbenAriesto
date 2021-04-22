class Siswa:
    jumlah_siswa = 0

    def __init__(self, nama, kelas, alamat, nilai, usia):
        self.nama = nama
        self.kelas = kelas
        self.alamat = alamat
        self.nilai = nilai
        self.usia = usia
        Siswa.jumlah_siswa += 1
    
    def viewSiswa(self):
        print("----------")
        print("Data Siswa")
        print("Nama:", self.nama)
        print("Kelas:", self.kelas)
        print("Alamat:", self.alamat)
        print("Usia:", self.usia)
        print("----------")
    
    def viewNilai(self):
        print("Data Nilai")
        print("Nama:", self.nama)
        for nilai in self.nilai:
            print("Nilai:", nilai)
        print("----------")
    
    def viewKeterangan(self):
        print("Keterangan")
        print("Nama:", self.nama)
        print("Kelas:", self.kelas)
        rata = sum(self.nilai) / len(self.nilai)
        print("Rata-rata:", rata)
        if rata >= 75:
            keterangan = "Lulus"
        else:
            keterangan = "Tidak lulus"
        print("Keterangan:", keterangan)
        print("----------")

siswa1 = Siswa("Finda", "XII MIPA 1", "Magelang", [89, 67, 85, 47], 17)
siswa2 = Siswa("Umi", "XII MIPA 2", "Bantul", [89, 97, 85, 87], 18)
siswa3 = Siswa("Budi", "XII MIPA 3", "Sleman", [78, 83, 96, 61], 17)

siswa1.viewSiswa()
siswa1.viewNilai()
siswa1.viewKeterangan()

siswa2.viewSiswa()
siswa2.viewNilai()
siswa2.viewKeterangan()

siswa3.viewSiswa()
siswa3.viewNilai()
siswa3.viewKeterangan()
print("Jumlah siswa:", Siswa.jumlah_siswa)