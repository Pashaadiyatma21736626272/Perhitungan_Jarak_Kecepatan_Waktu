import Rumus 

Kecepatan = Rumus.Kecepatan()
Jarak = Rumus.Jarak()
Waktu = Rumus.Waktu()

while True :
  print("===== Perhitungan Kecepatan,Jarak Dan Waktu =====")

  pilihan_user = input("Masukkan Pilihan:")
  if pilihan_user == "Kecepatan":
    Kecepatan()
  elif pilihan_user == "Jarak":
    Jarak()
  elif pilihan_user == "Waktu":
    Waktu()
  else:
    exit()




