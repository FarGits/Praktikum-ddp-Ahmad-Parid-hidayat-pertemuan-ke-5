#==== 1 ====
kendaraan =['GTR', 'mobil', '5000', 'biru', '2']
print(kendaraan)

kendaraan.append('1M')
kendaraan.append('Gigi')
print(kendaraan)

kendaraan.insert(2,'BMW')
print(kendaraan)

print(type(kendaraan))
print(type(kendaraan[0]))
print(type(kendaraan[1]))
print(type(kendaraan[2]))
print(type(kendaraan[3]))
print(type(kendaraan[4]))
print(type(kendaraan[5]))
print(type(kendaraan[6]))

#==== 2 ====

pilihan = int(input("Masukkan pilihan (1: persegi, 2: lingkaran, 3: segitiga): "))

match pilihan:
    case 1:
        sisi = float(input("Masukkan panjang sisi persegi: "))
        luas = sisi * sisi
        print("Luas persegi:", luas)
    case 2:
        jari_jari = float(input("Masukkan jari-jari lingkaran: "))
        luas = 3.14 * jari_jari * jari_jari
        print("Luas lingkaran:", luas)
    case 3:
        alas = float(input("Masukkan panjang alas segitiga: "))
        tinggi = float(input("Masukkan tinggi segitiga: "))
        luas = 0.5 * alas * tinggi
        print("Luas segitiga:", luas)
    case _:
        print("Pilihan tidak valid")
