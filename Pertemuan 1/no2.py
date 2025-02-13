temp = float(input('Masukan suhu dalam celcius: '))

if temp < 0:
    print('Membeku')
elif temp < 10:
    print('Sangat Dingin')
elif temp < 20:
    print('Sejuk')
elif temp < 30:
    print('Hangat')
elif temp < 40:
    print('Panas')
elif temp >= 40:
    print('Sangat Panas')