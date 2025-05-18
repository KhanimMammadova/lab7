massiv = [-3, 0, -5, -2, 4, 7, -1]
with open("ededler.txt", "w") as file:
    for eded in massiv:
        file.write(str(eded) + "\n")
with open("ededler.txt", "r") as file:
    ededler = [int(satir.strip()) for satir in file]
yeni_massiv = []
for eded in ededler:
    if eded > 0:
        break
    yeni_massiv.append(eded)
with open("yeni_ededler.txt", "w") as yeni_file:
    for eded in yeni_massiv:
        yeni_file.write(str(eded) + "\n")
hasil = 1
for eded in yeni_massiv:
    hasil *= eded
print("Birinci müsbət elementdən əvvəlki ədədlərin hasili:", hasil)
