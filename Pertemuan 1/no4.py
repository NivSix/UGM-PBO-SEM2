angka = int(input('masukan angka: '))

def cek_prima(n):
    if angka < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if angka % i == 0:
            return False
    return True

if cek_prima(angka):
    print("Angka prima")
else:
    print("Bukan angka prima")