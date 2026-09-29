# Uzdevums: Kalkulators
# Lietotājam jāievada divi skaitļi un darbības zīme
# (piem. saskaitīšana, atņemšana, dalīšana vai reizināšana)
# Un programmai ir jāizvada darbības rezultāts
# rezultāts = 0
# skaitlis1 = float(input("Skaitlis: "))
# skaitlis2 = float(input("Skaitlis: "))
# darb_zime = input("Darbības zīme: ")
# if darb_zime == "+":
#     rezultāts = skaitlis1 + skaitlis2
# elif darb_zime == "-":
#     rezultāts = skaitlis1 - skaitlis2
# elif darb_zime == "*":
#     rezultāts = skaitlis1 * skaitlis2
# elif darb_zime == "/":
#     rezultāts = skaitlis1 / skaitlis2
# else:
#     print("Nezināma darbība!")
# print(f"{skaitlis1} {darb_zime} {skaitlis2} = {rezultāts}")
# If bloks izmantojot match-case
# match darb_zime:
#     case "+":
#         rezultāts = skaitlis1 + skaitlis2
#     case "-":
#         rezultāts = skaitlis1 - skaitlis2
#     case "*":
#         rezultāts = skaitlis1 * skaitlis2
#     case "/":
#         rezultāts = skaitlis1 / skaitlis2
#     case _:
#         print("Nezināma darbība")

# Cikli
# for - izmanto kādam zināmam diapazonam - piem. sarakstam
# t.i. ja vajag izpildīt darbību x reizes
# while - jebkurā situācijā, kad atkārtojam darbību vairākas reizes

saraksts = [ 123, 3566, 5342, 3123 ]
# ar for ciklu varam pāriet pāri katrai saraksta vērtībai
for vērtība in saraksts:
    # piem. katrā iterācijā tiek palaists viens print
    print(vērtība)
# cikls diapazonam no 0 līdz 9 - [0, 10)
# parametri - sākums (iekļauts), beigas (neiekļaus), solis
# piem. ja gribam katru otro skaitli - solis ir 2
for iii in range(0, 10, 2): 
    print(iii)

# Uzdevums: Dots sekojošs saraksts
saraksts = [ 123, 3566, 5342, 3123 ]
# lietotājs ievada skaitli, jums ir jāizvada šī skaitļa indekss
# ja tas ir sarakstā, "nav sarakstā", ja tas nav.
# saraksts[idx] == vert
ievade = int(input("Ievadāt skaitli: "))
atrasts = False
for idx in range(0, len(saraksts)): # katram indeksam sarakstā
    # katrā iterācijā pārbauda, vai ar noteiktajā indeksā sarakstā atrodās 
    # ievadītā vērtība
    if saraksts[idx] == ievade:
        print(f"Vērtība ir indeksā {idx}!")
        atrasts = True # ja ir atrasts - mēs uzglabājam par to informāciju
if not atrasts: # ja ne reizi netika atrasta vērtība - izvadam tekstu
    print("Vērtība sarakstā neeksistē (vērtība nav atrasta)!")
# Variants ar while ciklu
atrasts = False
idx = 0 # tiek nodefinēts ar sākuma vērtību ĀRPUS cikla
while idx < len(saraksts):
    if saraksts[idx] == ievade:
        print(f"Vērtība ir indeksā {idx}!")
        atrasts = True
    idx += 1 # cikla beigās tiek veikta pieskaitīšana mainīgajam idx
if not atrasts:
    print("Vērtība sarakstā neeksistē!")

# Svarīgi atslēgvārdi - cikla kontrole
# break - pārtrauc cikla darbību
# continue - pabeidz pašreizējo iterāciju - sāk nākošo
a = 0
while a < 15:
    a += 1
    # ja a ir 5, beidzam iterāciju - print netiks palaists, bet cikls turpinās
    if a == 5: 
        continue
    # ja a ir 9, beidzam ciklu - print netiks palaists, un 8 būs pēdējais
    # izvadītais skaitlis - 10-14 netiks izvadīti, jo cikls jau ir beidzies
    if a == 9: 
        break
    print(a)
print("Cikls beidzās!")

# Uzdevums: Uzrakstat ciklus, kas ļauj ievadīt sarakstā 3 jebkādas vērtības
# Realizējat divus ciklus - gan for, gan while
# For
saraksts = []
for iii in range(3):
    saraksts.append(input("Ievade: "))

# While - Pirmais veids
saraksts = []
iii = 0
while iii < 3:
    saraksts.append(input("Ievade: "))
    iii += 1
# While - otrais veids
saraksts = []
while len(saraksts) < 3:
    saraksts.append(input("Ievade: "))