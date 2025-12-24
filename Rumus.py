def Kecepatan():
  Jarak = int(input("Masukkan Jarak :"))
  Waktu = int(input("Masukkan Waktu :"))

  Kecepatan = Jarak / Waktu
  kecepatan = int(Kecepatan)
  print(f"Kecepatannya Adalah : {kecepatan}")

def Jarak():
  Kecepatan = int(input("Masukkan Kecepatan :"))
  Waktu = int(input("Masukkan Waktu :"))

  Jarak = Kecepatan * Waktu
  jarak = int(Jarak)
  print(f"Jaraknya Adalah : {jarak}")

def Waktu():
  Jarak = int(input("Masukkan Jarak :"))
  Kecepatan = int(input("Masukkan Kecepatan :"))

  Waktu = Jarak / Kecepatan
  waktu = int(Waktu)
  print(f"Waktunya Adalah : {waktu}")
