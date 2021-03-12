#menampilkan informasi program
print("menghitung luas persegi panjang")

#input nilai panjang dan lebar persegi panjang
P = float(input("masukkan nilai panjang: "))
L = float(input("masukkan nilai lebar: "))

#menghitung luas persegi panjang
Luas_persegi_panjang = P * L

#menampilkan hasil perhitungan luas persegi panjang
print("luas persegi panjang adalah", Luas_persegi_panjang)


#menampilkan informasi program
print("menghitung luas lingkaran")

#input nilai jari-jari lingkaran
r = float(input("masukkan nilai jari-jari:" ))
phi = float(input("masukkan phi: "))

#menghitung luas lingkaran
Luas_lingkaran = phi * r * r

#menampilkan hasil perhitungan luas lingkaran
print("luas lingkaran adalah", Luas_lingkaran)


#menampilkan informasi program
print("menghitung luas permukaan kubus")

#input nilai sisi permukaan kubus
s = float(input("masukkan nilai sisi: "))

#menghitung luas permukaan kubus
Luas_permukaan_kubus = 6 * s * s

#menampilkan hasil perhitungan luas permukaan kubus
print("luas permukaan kubus adalah", Luas_permukaan_kubus)


#menampilkan informasi program
print("konversi suhu celcius ke fahrenheit")

#input nilai suhu dalam celcius
C = float(input("masukkan nilai suhu dalam celcius: "))

#menghitunga hasil pengkonversian
C_F = 9 * (C + 32) / 5

#menampilkan hasil hitung pengkonversian
print("besar suhu dalam fahrenheit adalah", C_F)


#menampilkan informasi program
print("konversi suhu reamur ke kelvin")

#input nilai suhu dalam reamur
R = float(input("masukkan nilai suhu dalam reamur: "))

#menghitung hasil pengkonversian
R_K = 5 * (R + 273) / 4

#menampilkan hasil hitung pengkonversian
print("besar suhu dalam kelvin adalah", R_K)
