import math

def hitung_lingkaran():
    try:
        r = float(input("Masukkan jari-jari lingkaran: "))
        if r <= 0:
            print("Jari-jari harus lebih dari 0!")
            return
        
        keliling = 2 * math.pi * r
        luas = math.pi * r ** 2
        
        print(f"Keliling lingkaran: {keliling:.2f}")
        print(f"Luas lingkaran: {luas:.2f}")
    except ValueError:
        print("Masukkan angka yang valid!")

hitung_lingkaran()