class Siswa:

    def __init__(self, nis, nama, kelas):
        self.__nis = nis
        self.__nama = nama
        self.__kelas = kelas
    
    def getnis(self):
        return self.__nis
    
    def setnis(self, newnis):
        self.__nis = newnis

wawan = Siswa(16354, "Sopan Setiawan", "XI MIPA 1")

print(wawan.getnis())
wawan.setnis(10000)
print(wawan.getnis())