# f(a) = a * a
# f(1) = 1 * 1
# f(2) = 2 * 2
# def nosaukums(parametrs1, parametrs2):
#     print("Funkcija...")
#     print("Funkcija...")
#     print("Funkcija...")
#     if 0 == 0:
#         pass
#     return -1
# print(nosaukums(1, 1))
# nosaukums(1, 1)
# nosaukums(1, 1)

# Pielietojums
# 1. Samazina koda duplikāciju (praktiski obligāti - 2+ ja ir liels koda gabals, 3+ citos gadījumos)
# 2. Padara programmu lasāmāku
# Piemērs - Sarakstā ievada 5 vērtības, izvada šo skaitļu reizinājumu kvadrātā
# def ievadīt_skaitļus(skaitļu_skaits):
#     print("izsaukta ievadīšanas funkcija")
#     saraksts = []
#     for iii in range(skaitļu_skaits):
#         saraksts.append(int(input(f"ievadīt skaitli {iii}: ")))
#     return saraksts
# saraksts1 = ievadīt_skaitļus(5)
# saraksts2 = ievadīt_skaitļus(7)
# def izvadīt_skaitļus(saraksts):
#     print("Izsaukta izvadīšanas funkcija")
#     for skaitlis in saraksts:
#         print(skaitlis*skaitlis)
# saraksts = ievadīt_skaitļus(7)
# izvadīt_skaitļus(saraksts)
# 3. Abstraktēšana - Neņam procesus, un aprastam tos
# Piemērs - Naudas izņemšana no bankas konta, kas ir aprakstīta funkcijas formā
print("asd", "asd", "asd")

# Uzdevums: Uzrakstat funkciju, kas pieņem skaitli kā parametru
# Un atgriež True ja šis skaitlis ir pāra skaitlis, vai False
# ja skaitlis ir nepāra skaitlis

# Funkcijas definīcija
# def para_nepara(skaitlis):
#     # return skaitlis % 2 == 0
#     if skaitlis % 2 == 0:
#         return True
#     else:
#         return False
# para_nepara(2)   
    
# Funkcijas izsaukšana
# rezultāts = para_nepara(2)
# print(rezultāts)
# print(para_nepara(4))
# ievad_skaitlis = int(input("Ievadāt skaitli: "))
# print(para_nepara(ievad_skaitlis))

# Uzdevums: Uzrakstāt funkciju, kas pārbauda vai parametrs (skaitlis)
# ir lielāks, mazāks vai vienāds ar 0 un izvada pārbaudes rezultātu.
# def pārbaude(skaitlis):
#     if skaitlis > 0:
#         print("Skaitlis ir lielāks")
#     elif skaitlis < 0:
#         print("Skaitlis ir mazāks")
#     else:
#         print("Skaitlis ir 0")
# pārbaude(2)
# pārbaude(0)
# pārbaude(-1)

# Funkcijas kas izsauc pašas sevi - rekursīvās funkcijas
# def faktoriāls(skaitlis):
#     print(f"Izsaukts ar skaitli {skaitlis}")
#     if skaitlis == 1:
#         return 1
#     else:
#         return skaitlis * faktoriāls(skaitlis - 1)
# print(faktoriāls(5))

# Standarta vērtības - parametri kuri nav obligāti jānorāda
# ja tie netiks norādīti - tiks izmantota norādītā standarta vērtība
# var miksēt ar neobigātajiem parametriem
def funkcija(obligātais_param, parametrs = "standarta vērtība", parametrs2 = "cita vērtība"):
    print(obligātais_param)
    print(parametrs)
    print(parametrs2)
funkcija(1, parametrs2="atkal cita vērtība")
funkcija("obligātā vērtība", "ne-standarta vērtība")
#funkcija() # kļūda - nav definēts obligātais parametrs

#print("asd", "asd", "asd", "sda", "asd")
# ar vienu parametra definīciju, funkcija var pieņemt neierobežotu daudzumu vērtību
def neier_parametri(*parametri, parametrs2="Neobligātais parametrs"):
    print(parametri) # parametri ir Tuple (neizmaināms saraksts)
    print(parametrs2)
neier_parametri(12,123,3,4,34,234,123, parametrs2="asd")
# praktisks piemērs ar print -
# sep - atdalītājs, ja ir print ar vairākām vērtībām
# end - simbols kas tiek pievienots pēc teksta iekš print - standartā \n
# kas ir iemesls kādēļ katrs print aiziet jaunā rindā.
print("asd", "asd", "asd", "sda", "asd", sep=",", end="") 
print("asd", "asd", "asd", "sda", "asd", sep=",")

# Uzdevums: Uzrakstīt funkciju, kas pieņem neierobežotu daudzumu skaitļus
# Un izvada lielāko no tiem. Neizmantot funkciju max().
def lielākais(*skaitļi):
    rezultāts = skaitļi[0]
    for skaitlis in skaitļi:
        if rezultāts < skaitlis:
            rezultāts = skaitlis
    return rezultāts
print(lielākais(10,20,30,99,-1,5))