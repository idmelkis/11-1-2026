# Uzdevums: Prasāt lietotājam lai ievada 
# tā mīļāko dzīvnieku, ēdienu un valsti.
# Izvadat šo informāciju sekojošā formātā:
# Mīļākie:
# Dzīvnieks: {}
# Ēdiens: {}
# Valsts: {}
# dzivnieks = input("Ievadat mīļāko dzīvnieku: ")
# ediens = input("Ievadat mīļāko ēdienu: ")
# valsts = input("Ievadat mīļāko valsti: ")
# print("Mīļākie")
# print(f"Dzīvnieks: {dzivnieks}") # f""
# print(f"Ēdiens: {ediens}")
# print(f"Valsts: {valsts}")
# print("Dzīvnieks: " + dzivnieks)
# print("Dzīvnieks: ", dzivnieks)

# Uzdevums: Ir dots sekojošs saraksts
soma = [ "Zobens", "Vairogs", "Ūdens" ]
# Uzrakstat programmu, kas - ļauj lietotājam izņemt vienu no elementiem no somas
# Izvadat izņemto elementu, un somas saturu pēc izņemšanas.
# Ir divi varianti - vai nu ar list.pop(idx), vai list.remove(str)!
# === pop
# soma = [ "Zobens", "Vairogs", "Ūdens" ]
# idx = int(input("Ievadat kuru vērtību gribat izņemt: ")) # int() - pārveido par skaitli
# print(f"Izņemtais elements: {soma[idx]}")
# soma.pop(idx)
# print(soma)
# === remove
# soma = [ "Zobens", "Vairogs", "Ūdens" ]
# iznemt = input("Ievadat ko gribat izņemt: ")
# soma.remove(iznemt)
# print(f"Izņemtais elements: {iznemt}")
# print(soma)

# if/else - loģiskās pārbaudes
# Kods zem if ir jābūt ar atstarpēm (space/tabs) no kreisās puses
# Atstarpju daudzumu var konfigurēt - standarts - 4 atstarpes
#if <loģiskā pārbaude>:
    # šeit ir kods (4 atstarpes)
    #if <loģiskā pārb>:
        # šeit ir kods nākošajam if (vēl 4 atstarpes)
    #  šis kods tiks izpildīts zem pirmā if (4 atstarpes)
# šeit turpinās kods kas nav zem if
if False:
    pass # pass = nedarīt neko
elif True: # else if (elif) izpildās ja neizpildās iepriekšējā pārbaude
    pass
elif True: # var būt neierobežots skaits
    pass
else: # else izpildās ja neizpildās neviena no iepriekšējām pārbaudēm
    pass
# switch/match - var lietot gadījumos, kad ir viens mainīgais kuram vajag
# pārbaudīt vairākas vērtības
skaitlis = 15
if skaitlis == 10:
    print("Izpildās tikai, ja skaitlis ir 10")
elif skaitlis == 11:
    print("Izpildās tikai, ja skaitlis ir 11")
else:
    print("Izpildās tikai, ja skaitlis nav ne 10, ne 11")
# ir vienāds ar
match skaitlis:
    case 10: # īsāk - nav jāraksta ==
        print("Izpildās tikai, ja skaitlis ir 10")
    case 11:
        print("Izpildās tikai, ja skaitlis ir 11")
    case _:
        print("Izpildās tikai, ja skaitlis nav ne 10, ne 11")

# Loģiskās pārbaudes
# Vienādojums - abas vērtības ir vienādas - == ( piem. 10 == 10 )
# Nevienādojums - abas vērtības NAV vienādas - != ( piem 11 != 10 )
# Lielāks - kreisā puse ir lielāka par labo - > ( piem. 10 > 9 )
# Mazāks - kreisā puse ir mazāka par labo - < ( piem. 9 < 10 )
# Lielāks vai vienāds - kreisā puse ir lielāka VAI vienāda ar labo - >= ( piem. 10 >= 10)
# Mazāks vai vienāds - kreisā puse ir mazāka VAI vienāda ar labo - >= ( piem. 10 <= 10)
# Vienāda vērtība un datu tips - is ( piem. 10 is 10 ) - pārbauda objekta tipu
# Negatīvā pārbaude - not (piem. not 10 == 10 izvadīs False)

# Dalāmība (Modulus) - Izvada dalīšanas atlikumu - %
# Piemērs 10 % 5 - atlikums ir 0, attiecīgi dalās 
# 10 % 5 == 0
# Piemērs 10 % 3 - atlikums ir 1, skaitlis nedalās

# Uzdevums: Lietotājam jāievada skaitlis, un programmai ir jāizvada 
# "Jā", ja skaitlis ir MAZĀKS par 10, "Nē", ja skaitlis ir lielāks par 10.
ievade = int(input("Skaitlis: "))
if ievade < 10:
    print("Jā")
elif ievade > 10:
    print("Nē")
else:
    print("Skaitlis ir 10")

# Loģisko pārbaužu apvienošana
if ievade > 10 and ievade < 20: # AND - darbībām abās pusēs jāizpildās
    print("Ievade ir lielāka par 10, bet mazāka par 20")
if ievade > 10 or ievade < 5: # OR - jāizpildās tikai vienai no darbībām
    print("Ievade ir vai nu lielāka par 10, vai mazāka par 5")

# Jūs varat izmantot iekavas lai vizuāli atdalītu dažādas pārbaudes
#if (ievade > 10 or ievade < 5) and (ievade > 90 or ievade < 20): 
#    pass

# Uzdevums: Izveidojat biļešu cenu kalkulatoru
# Bērniem zem 12 gadiem, cena ir €5
# Skolēniem (12-17), cena ir €8
# Pieaugušajiem (18-65), cena ir €15
# Senioriem (65+), cena ir €8
# Lietotājam jāievada vecums un programmai ir jāizvada biļetes cena.
ievade = int(input("Vecums: "))
cena = 0
if ievade < 12:
    cena = 5
elif ievade >= 12 and ievade <= 17:
    cena = 8
elif ievade >= 18 and ievade <= 65:
    cena = 15
elif ievade > 65:
    cena = 8
print(f"Biļetes cena ir €{cena}!")
