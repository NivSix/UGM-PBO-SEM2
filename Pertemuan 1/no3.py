def hitung_nilai():
    while True:
        niu = int(input("Masukkan NIU (6 digit): "))
        if 100000 <= niu <= 999999:
            break
        else:
            print("NIU harus 6 digit!")
       
    tugas = float(input("Masukkan nilai tugas: "))
    laporan = float(input("Masukkan nilai laporan: "))
    
    rata_rata = (tugas + laporan) / 2

    if rata_rata < 40:
        print("Nilai huruf: K")
    
    ujian = float(input("Masukkan nilai ujian: "))
    
    nilai_akhir = (0.25 * tugas) + (0.25 * laporan) + (0.5 * ujian)
    
    if 80 <= nilai_akhir <= 100:
        nilai_huruf = "A"
    elif 70 <= nilai_akhir < 80:
        nilai_huruf = "B"
    elif 60 <= nilai_akhir < 70:
        nilai_huruf = "C"
    elif 50 <= nilai_akhir < 60:
        nilai_huruf = "D"
    else:
        nilai_huruf = "E"
    
    print(f"Nilai akhir: {nilai_akhir:.2f}")
    print(f"Nilai huruf: {nilai_huruf}")

hitung_nilai()