tabel = []
no = 0
while True:
    n = input("Nama : ")
    N = input("NIM : ")
    tugas = int(input("Nilai Tugas : "))
    uts = int(input("Nilai UTS : "))
    uas = int(input("Nilai UAS : "))
    jawab = input("Tambah data(Ya/Tidak)? ")
    a = int(tugas*30/100)
    b = int(uts*35/100)
    c = int(uas*35/100)
    akhir = a+b+c
    no = no+1
    tabel.append([n, N, tugas, uts, uas, akhir, no])
    if jawab == "tidak":
        break
print("===================================================================================")
print("| No. |     Nama     |      NIM     |   Tugas   |   UTS   |   UAS   |    Akhir    |")
print("===================================================================================")
for x in tabel:
    print("|  {No:2} |  {Nama:10}  |  {NIM:10}  |   {Tugas:5}   |   {UTS:3}   |   {UAS:3}   |    {Akhir:3.2f}    |".format(Nama=x[0], NIM=x[1], Tugas=x[2], UTS=x[3], UAS=x[4], Akhir=x[5], No=x[6]))
print("===================================================================================")