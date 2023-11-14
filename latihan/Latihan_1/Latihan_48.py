print("===================== Bagian A =====================")
print("Menampilkan Bilangan Genap dari 2 - 100")
print("Cara 1")

genap = range(2, 101, 2)
for x in genap:
    print(f"ini hasilnya : {x}")

print("Cara 2")

countGenap = int(input("Kasih angka biar hasil genap : ")) # 0
while (countGenap < 100):
    countGenap = countGenap + 2
    print(f"Hasilnya : {countGenap}")

# ===========================================================

print("===================== Bagian B =====================")
print("Menampilkan Bilangan Ganjil dari 99 - 1")
print("Cara 1")

ganjil = range(99, 0, -2)
for i in ganjil:
    print(f"ini hasilnya : {i}")

print("Cara 2")

countGanjil = int(input("Kasih angka biar hasil ganjil : ")) # 101
while (countGanjil > 1):
    countGanjil = countGanjil - 2
    print(f"Hasilnya : {countGanjil}")