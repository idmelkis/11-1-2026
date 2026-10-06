# Uzdevums: Uzrakstat ciklu, kas izvada skaitļus 
# no 0 līdz 10 izlaižot skaitļus 4 un 6
# Realizēt gan while gan for cikla variantus.
# for
# for iii in range(0,11):
#     if iii == 4 or iii == 6:
#         continue
#    print(iii)

#    if iii != 4 or iii != 6:
#        print(iii)
# while
# skaitītājs = -1
# while skaitītājs <= 10:
#     skaitītājs += 1
#     if skaitītājs == 4 or skaitītājs == 6:
#         continue
#     print(skaitītājs)

# Uzdevums: Ir dots saraksts
saraksts = [ 0, 5, 4, 9, 10, 12 ]
# Neizmantojot funkciju sum(), uzrakstat ciklu, kas saskaita
# visas vērtības šajā sarakstā un izvada rezultātu.
rezultāts = 0
for vērtība in saraksts:
    rezultāts += vērtība
print(rezultāts)

# Uzdevums: aprēķini faktoriāli lietotāja ievadītajam skaitlim
# Faktoriālis - skaitlis kas veidojas reizinot visus skaitļus no
# 1 līdz n., t.i. 3! == 1*2*3 = 6.
# Piezīme - 0! == 1.
# Uzrakstat programmu kas veic šo aprēķinu.
ievade = int(input("Skaitlis: "))
# N.B. Tehniski šis if nav vajadzīgs, jo range jau tā būs no 1 līdz 1
if ievade == 0:
    print("1")
else:
    rezultāts = 1
    for iii in range(1, ievade + 1):
        rezultāts *= iii
    print(rezultāts)

# Uzdevums: Jums ir mainīgais, kas satur kaut kādu paroli
parole = "RAVGParole!"
# Uzrakstat ciklu, kas prasīs lietotājam ievadīt paroli līdz ir ievadīta pareiza parole.
# Ja parole nav ievadīta pareizi, izvadāt "Nepareiza Parole"
# 1. var
# ievade = input("Parole")
# while parole != ievade:
#     print("Nepareiza parole")
#     ievade = input("Parole")
# 2. var
while True:
    ievade = input("Parole")
    if ievade != parole:
        print("Nepareiza parole")
    else:
        break
print("Parole ievadīta pareizi!")

# Uzdevums: Tiek ģenerēts nejaušs skaitlis
import random
skaitlis = random.randint(0, 100)
# Jāuzraksta cikls, kurā lietotājs ievada skaitli.
# Programma pārbauda vai skaitlis ir uzminēts,
# ja nav, izvada, vai ievadītais skaitlis ir lielāks, 
#  vai mazāks par nejaušo skaitli.
# Kad lietotājs ir uzminējis skaitli - 
# Cikls beidzās, izvadīt 'Uzvara'
while True:
    ievade = int(input("Skaitlis: "))
    if ievade == skaitlis:
        break
    elif ievade < skaitlis:
        print("Skaitlis ir lielāks")
    else:
        print("Skaitlis ir mazāks")
print("Uzvara")

# i/ni darbs
# Uzrakstīt ciklu, kas iet pāri skaitļiem no 1, līdz 100, un 
# ja skaitlis dalās ar 3, izvada vārdu "Fizz"
# Ja skaitlis dalās ar 5, izvada vārdu "Buzz"
# Ja skaitlis dalās ar 3 UN 5, izvada "FizzBuzz"
# Ja skaitlis nedalās ar nevienu no šiem skaitļiem, Izvadāt šo skaitli
# Dalīšanas atlikuma pārbaudei izamntot - % - modulus operatoru

# Modulus operators - izvada dalīšanas atlikumu, piem. 
# 5 % 2 == 1
# 7 % 3 == 1
# Šo var izmantot, lai pārbaudītu, vai skaitlis dalās ar 
# citu skaitlis (izvadīs 0).
# 6 % 3 == 0
# N.B.  šī ir darbība - tā pat kā citas (skaitīšana, reizināšana utt.)
# Lai pārbaudītu vērtību jāizmanto ==, >, < u.tt.