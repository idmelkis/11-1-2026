# Datu tipi
# Kāda veida informāciju varam uzglabāt mainīgajos
# 1. Teksts (string)
# 2. Veseli skaitļi (integer)
# 3. Daļskaitļi (float/double)
skaitlis = 5 + 0.5 + 0.5 # 6.0
print(skaitlis)
# 4. Loģiskie predikāti - Boolean - 
#    True/False (Patiess/Nepatiess)
rezultāts = skaitlis == 6.0 # True
rezultāts = skaitlis == 6.1 # False
# 5. Saraksti (list)
saraksts = [ "pirmais elements", 2, True, 2.0 ]
sensora_dati = [ 0.5, 0.1, 0.6, 0.7 ]

rezultāts = 4 + 4 # 8
rezultāts = 4 * 4 # 16
# rezultāts = 4 + "4" # Kļūda - skaitli ar tekstu nevar jaukt!
rezultāts = str(rezultāts) + "4" # "44"
print(rezultāts)
rezultāts = 4 * "4" # "4444"
print(rezultāts)

print(10*"*")
print("rezultāts = 10")
print(10*"*")

# Formatēts teksts
rezultāts = 4444
teksts = "rezultāts = " + str(rezultāts)
teksts = f"rezultāts = {rezultāts}"
print(teksts)
teksts = f"rezultāts = {4 + 4}"
print(teksts)
teksts = f"rezultāts = {4 == 4}"
print(teksts)
print("rezultāts = " + str(rezultāts))
print("rezultāts =", rezultāts, "!")
print(f"rezultāts = {4 == 4}, {1+1}") # Vairāku mainīgo izvade
# Izvade vairākās rindās
print("Hello World!\nJauna rinda")
# Burtiska izvade - iekļauj jaunas rindas
print("""Pirmā rinda
Otrā rinda""")

# Saraksti
sensora_dati = [ 0.5, 0.1, 0.6, rezultāts ]
# 3D matricas
# 1 2 3
# 4 5 6
# 6 5 4
matrica = [ [ 1, 2, 3 ], [ 4, 5, 6 ], [ 6, 5, 4 ] ]

sensora_dati = [ 0.5, 0.1, 0.6 ]
print(sensora_dati)
sensora_dati.append(1.0) # Ievieto elementu saraksta beigās!
print(sensora_dati)
sensora_dati.insert(0, 5.0) # Ievieto elementu saraksta sākumā!
sensora_dati.insert(0, 5.0) # Ievieto elementu saraksta sākumā!
print(sensora_dati)
sensora_dati.insert(2, 9.0) # Ievieto elementu saraksta 3 pozīcijā!
print(sensora_dati)
sensora_dati.insert(-1, 10.0) # ievietos kā priekšpēdējo elementu
print(sensora_dati)

sensora_dati.remove(5.0) # Izņem vērtību 5.0 no saraksta. 
                         #Izņem tikai vienu šādu vērtību!
print(sensora_dati)
sensora_dati.pop(0) # Izņem vērtību pēc indeksa (pirmo)
print(sensora_dati)
sensora_dati.pop(-1) # Izņem vērtību pēc indeksa (pēdējo)
print(sensora_dati)
print(len(sensora_dati)) # Atgriež saraksta garumu
print(sensora_dati[0]) # Atgriež pirmo skaitli
print(sensora_dati[-1]) # Atgriež pēdējo skaitli
print(sensora_dati[1:-1]) # Atgriež no pirmā indeksa 
                          # līdz pirmspēdējam [0.5, 0.1, 0.6]
print(sensora_dati[1:len(sensora_dati)-1]) # Atgriež no pirmā indeksa 
                                           # līdz pirmspēdējam [0.5, 0.1, 0.6]
print(sensora_dati[1:3]) # Atgriež no pirmā līdz 
                         # trešajam skaitlim [0.5, 0.1]

kortezs = ( 0.1, 0.5 ) # Tuple
# kortezs.append(0.1) # KĻŪDA - kortežiem nevar pievienot 
                      # vērtības pēc to definīcijas

# Tekstu var indeksēt tieši tā pat kā sarakstus
teksts = "Teksts"
teksta_garums = len(teksts) # 6
teksta_burts = teksts[1:-1] # ekst
print(teksta_burts)

# Nākošajā stundā - uzdevumi (ievade/izvade, saraksti)
#                   if/else (loģika, salīdzināšana)