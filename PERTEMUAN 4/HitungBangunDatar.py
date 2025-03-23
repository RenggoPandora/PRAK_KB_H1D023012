import math
import time


def lingkaran():
    r = float(input("Masukkan jari-jari lingkaran: "))
    luas = math.pi * r**2
    keliling = 2 * math.pi * r
    print(f"Luas: {luas:.2f}, Keliling: {keliling:.2f}")


def persegi():
    sisi = float(input("Masukkan panjang sisi persegi: "))
    luas = sisi ** 2
    keliling = 4 * sisi
    print(f"Luas: {luas:.2f}, Keliling: {keliling:.2f}")


def persegi_panjang():
    panjang = float(input("Masukkan panjang: "))
    lebar = float(input("Masukkan lebar: "))
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    print(f"Luas: {luas:.2f}, Keliling: {keliling:.2f}")


def segitiga():
    alas = float(input("Masukkan panjang alas: "))
    tinggi = float(input("Masukkan tinggi: "))
    luas = 0.5 * alas * tinggi
    print(f"Luas: {luas:.2f}")


while True:
    print("\nMenu Kalkulator Geometri:")
    print("1. Lingkaran")
    print("2. Persegi")
    print("3. Persegi Panjang")
    print("4. Segitiga (hanya luas)")
    print("5. Keluar")

    pilihan = input("Pilih bentuk (1-5): ")

    if pilihan == "1":
        lingkaran()
    elif pilihan == "2":
        persegi()
    elif pilihan == "3":
        persegi_panjang()
    elif pilihan == "4":
        segitiga()
    elif pilihan == "5":
        print("Keluar dari program...")
        time.sleep(1)
        break
    else:
        print("Pilihan tidak valid, coba lagi!")
