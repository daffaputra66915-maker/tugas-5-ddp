print("Program Menghitung Luas Bangun Datar")
print("1. Persegi")
print("2. Lingkaran")
print("3. Segitiga")

hitung = int(input("Memilih Program (1/2/3): "))

match hitung:
    case 1:
        sisi = float(input("Masukkan panjang sisi: "))
        luas = sisi * sisi
        print("Luas persegi =", luas)

    case 2:
        r = float(input("Masukkan jari-jari lingkaran: "))
        luas = 3.14 * r * r
        print("Luas lingkaran =", luas)

    case 3:
        alas = float(input("Masukkan alas segitiga: "))
        tinggi = float(input("Masukkan tinggi segitiga: "))
        luas = 0.5 * alas * tinggi
        print("Luas segitiga =", luas)

    case _:
        print("SALAH PILIH")
